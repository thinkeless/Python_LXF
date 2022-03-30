def try_to_change_list_content(the_list):
    print('got', the_list)
    the_list.append('study')
    print('change', the_list)

org_list = ['cheng', 'xin', 'hua']


def try_to_change_list_reference(the_list):
    print('got', the_list)
    the_list = ['cheng', 'xin', 'hua', 'study', 'python']
    print('change', the_list)

print('bef_list', org_list)
try_to_change_list_reference(org_list)
print('after_list', org_list)
print("------------------------------")
print('bef_list', org_list)
try_to_change_list_content(org_list)
print('after_list', org_list)
