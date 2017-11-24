ErrorCode = {
    100: 'Wrong Request Json Data',
    101: 'Authentication Failed',
    400: 'Bad Request',
    # 403: 'Forbidden',

    404: 'Not Found',
    405: 'Method Not Allowed',
    500: 'Internal Server Error'
}

JsEfsClusterStatus = {
    'ServerName': None,
    "Node": [None, None],
    "HaStatus": None,
    'AgentVersion': None
}

JsEfsExport = {
    'Message': False,  # or True
    'Status': None,
    'Data': []
}

JsEfsExportData = {
    "ServerName": None,
    "ExportName": None,
    "ExportPath": None,
    "ServiceIp": None,
    "Proto": None,  # cifs or nfs
    "SecString": {
        "ClientSpec": None,
        "RW": None,
        "User": None,  # root or nobody
        "Mode": None  # sync or async
    }
}

JsEfsServer = {
    "Message": False,  # or True
    "Status": None,
    "Data": {
        "ServerName": None,
        "ServerIp": None,
        "Proto": None,  # cifs or nfs
        "Node": None,  # node1 or node2
        "ServiceIp": None,  # vip
        "AdminIp": None,
        "Pools": []  # vdb or vdc
    }
}

JsEfsServerRoute = {
    "ServerName": None,
    "Data": []
}

JsEfsServerRouteData = {
    'Destination': None,
    'Gateway': None,
    'Genmask': None,
    'Flags': None,
    'Metric': None,
    'Ref': None,
    'Use': None,
    'Iface': None
}

JsEfsServerInterface = {
    "ServerName": None,
    "Data": []
}

JsEfsServerInterfaceData = {
    "InfName": None,
    "Mtu": None,
    "MacAddr": None,
    "State": None,
    "Body": []
}

JsEfsServerInterfaceBody = {
    "Addr": None,
    "Netmask": None,
    'Broadcast': None,
    "Type": None  # service ip / local ip / admin ip
}

JsEfsPool = {
    "Message": False,  # or True
    "Status": None,
    "Data": []
}

JsEfsPoolData = {
    "ServerName": None,
    "PoolName": None,
    "Backend": None,  # ????
    "SizeTotal": None,
    "SizeAssign": None,
    "SizeFree": None,
    "SizeUsage": None,
}

JsEfsVol = {
    "Message": False,  # or True
    "Status": None,
    "Data": []
}

JsEfsVolData = {
    "ServerName": None,
    "VolName": None,
    "VolPath": None,
    "VolType": None,
    "VolOptions": None,
    "VolStatus": None,
    "ExportName": None,
    "ExportPath": None,
    "QosPolicy": None,
    "SizeTotal": None,
    "SizeAssign": None,
    "SizeFree": None,
    "SizeUsage": None,
    "InodeUsed": None,
    "InodeFree": None,
    "InodeUsage": None
}
