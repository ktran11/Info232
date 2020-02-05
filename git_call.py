from subprocess import call


def git_branch_tmp():
    ret_code = call(['git', 'branch', 'tmp'])
    assert ret_code == 0, 'git branch tmp FAILED (code={}) !'.format(ret_code)

def git_checkout_tmp():
    ret_code = call(['git', 'checkout', 'tmp'])
    assert ret_code == 0, 'git checkout tmp FAILED (code={}) !'.format(ret_code)

def git_checkout_TP(tp="TP0"):
    ret_code = call(['git', 'checkout', tp])
    assert ret_code == 0, 'git checkout {} FAILED (code={}) !'.format(tp, ret_code)

def git_checkout_master():
    ret_code = call(['git', 'checkout', 'master'])
    assert ret_code == 0, 'git checkout master FAILED (code={}) !'.format(ret_code)

def git_checkout_teacher():
    ret_code = call(['git', 'checkout', 'teacher'])
    assert ret_code == 0, 'git checkout teacher FAILED (code={}) !'.format(ret_code)

def git_fetch_remote(remote_name):
    ret_code = call(['git', 'fetch', remote_name])
    assert ret_code == 0, 'git fetch {} (code={}) !'.format(remote_name, ret_code)

def git_fetch_remote_master(remote_name):
    ret_code = call(['git', 'fetch', remote_name, 'master'])
    assert ret_code == 0, 'git fetch {} (code={}) !'.format(remote_name, ret_code)

def git_reset_remote_master(remote_name):
    ret_code = call(['git', 'reset', '{}/master'.format(remote_name)])
    assert ret_code == 0, 'git reset {}/master FAILED (code={}) !'.format(remote_name, ret_code)

def git_reset_remote_teacher(remote_name):
    ret_code = call(['git', 'reset', '{}/teacher'.format(remote_name)])
    assert ret_code == 0, 'git reset {}/teacher FAILED (code={}) !'.format(remote_name, ret_code)

def git_remote_add_info232(remote_name):
    depot_url = "https://github.com/{}/info232.git".format(remote_name)
    ret_code = call(['git', 'remote', 'add', remote_name, depot_url])
    assert ret_code == 0, 'git remote add {} FAILED (code={}) !'.format(remote_name, ret_code)

def git_remote_add_FakeClass(remote_name):
    depot_url = "https://github.com/{}/FakeClass.git".format(remote_name)
    ret_code = call(['git', 'remote', 'add', remote_name, depot_url])
    assert ret_code == 0, 'git remote add {} FAILED (code={}) !'.format(remote_name, ret_code)

def git_delete_branch_tmp():
    ret_code = call(['git', 'branch', '-d', 'tmp'])
    assert ret_code == 0, 'git branch tmp FAILED (code={}) !'.format(ret_code)


def clean_TP(TP="TP0"):
    ret_code = call(['rm', TP, '-rf'])
    assert ret_code == 0, 'rm {} -rf FAILED (code={}) !'.format(TP, ret_code)
    git_checkout_TP(TP)

