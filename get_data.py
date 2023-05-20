import requests


def log_in(session: requests.Session):
    with open('login.txt', 'r') as f:
        username, password = f.read().split('\n')

    payload = {
        'menuopenflag': 'N',
        'Selected_Action': 'login',
        'Menu_Item_ID': 49792,
        'Form_ID': 7323,
        'Pass': 1,
        'Stack': 1,
        'ChildRowID': 0,
        'Current_URL': 'https://www.troopwebhost.org/formCustom.aspx?Menu_Item_ID=49792&Custom_Form_ID=1',
        'User_Login': username,
        'User_Password': password,
        'Language_ID': 1,
        'Page_Layout': 1,
        'Report_option': 2,
        'Custom_Form_ID': 1,
        'FirstControl': 'User_Login',
    }

    cookies = {
        'Application_ID': '1338',
    }

    login_url = 'https://www.troopwebhost.org/formCustom.aspx'

    p = session.post(login_url, data=payload)
    assert('Log Off' in p.text)
    return p



with requests.Session() as session:
    session.cookies.set('Application_ID', '1338')
    p = log_in(session)



