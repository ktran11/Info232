# coding: utf-8
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import sys
import os
import argparse

import pandas as pd

from importlib import import_module
from importlib import invalidate_caches
from importlib import reload as reload_module
from teacher import grade
from students import get_students

from git_call import git_branch_tmp
from git_call import git_checkout_teacher
from git_call import git_checkout_tmp
from git_call import git_checkout_TP
from git_call import git_reset_remote_master
from git_call import git_reset_remote_teacher
from git_call import git_fetch_remote
from git_call import git_delete_branch_tmp
from git_call import clean_TP


def parse_args(main_description="Grading script to grade all registered students"):
    parser = argparse.ArgumentParser(description=main_description)
    parser.add_argument('TP', help='Which TP (directory) to grade', type=str)
    args = parser.parse_args()
    return args


def run(remote_name, answer, question, TP='TP0'):
    results = {}
    status  = {}
    try:
        git_fetch_remote(remote_name)
        git_reset_remote_master(remote_name)
        git_checkout_TP(TP)
        try:
            answer = reload_module(answer)
            print("="*80)
            results, status = grade(question, answer)
            print("="*80)
        except Exception as e:
            print(e)
    except AssertionError:
        pass
    results['name'] = remote_name
    status['name'] = remote_name
    return results, status


def main():
    args = parse_args()
    TP = args.TP
    GRADE_DIR = 'GRADES'
    os.makedirs(GRADE_DIR, exist_ok=True)
    
    # FIXME ugly hack to access student code if they forgot to use relative import
    sys.path.append('./{}'.format(TP))

    STUDENTS = get_students()
    git_branch_tmp()
    git_checkout_tmp()
    try :
        question = import_module('{}.questions'.format(TP))
        answer = import_module('{}.answers'.format(TP))
        all_results = [run(remote_name, answer, question, TP) for student_name, remote_name in STUDENTS.items()]
        all_scores = [e[0] for e in all_results]
        all_status = [e[1] for e in all_results]
        score_table = pd.DataFrame(all_scores)
        status_table = pd.DataFrame(all_status)
        score_path = os.path.join(GRADE_DIR, '{}-scores.csv'.format(TP))
        status_path = os.path.join(GRADE_DIR, '{}-status.csv'.format(TP))
        score_table.to_csv(score_path)
        status_table.to_csv(status_path)
    except AssertionError:
        pass
    finally:
        git_reset_remote_teacher("origin")
        clean_TP(TP)
        git_checkout_teacher()
        git_delete_branch_tmp()



if __name__ == '__main__':
    main()
