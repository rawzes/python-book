import win32serviceutil


def is_service_running(service):
    state = win32serviceutil.QueryServiceStatus(service)[1]
    states = {4: 'running', 2: 'stopping', 1: 'stopped'}
    print('{} state is {}'.format(service, states[state]))
    return state


def service_do_action(service, action):
    if action == 'stop':
        win32serviceutil.StopService(service)
        print('{} is stopping'.format(service))
    elif action == 'start':
        win32serviceutil.StartService(service)
        print('{} is starting'.format(service))
    elif action == 'restart':
        win32serviceutil.RestartService(service)
        print('{} is restarting'.format(service))
    else:
        return "unknown command"


if  __name__ == '__main__':
    service = 'SNMPTRAP'
    is_service_running(service)
    service_do_action(service, 'stop')
    is_service_running(service)
