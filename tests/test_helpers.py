records_from_csv = [
    {
        "ACW": "7",
        "ADDR": "20.128.243.133",
        "AGENT_NAME": "Scott Lopez",
        "CALL_ID": "971-605-3989x98841",
        "CUSTOMER_NAME": "Lisa Rosales",
        "END": "08/02/2020 9:23:25 AM",
        "ID": "84ef8-bfede-7972af",
        "START": "08/02/2020 9:12:26 AM",
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3 rv:3.0; ar-IL) AppleWebKit/531.8.1 (KHTML, like Gecko) Version/4.0.1 Safari/531.8.1",
    },
    {
        "ACW": "7",
        "ADDR": "105.0.200.198",
        "AGENT_NAME": "Paul Duncan",
        "CALL_ID": "001-634-775-4898x281",
        "CUSTOMER_NAME": "Sean Allen",
        "END": "08/05/2020 5:59:30 PM",
        "ID": "aad94-4669d-e72ece",
        "START": "08/05/2020 5:49:10 PM",
        "USER_AGENT": "Mozilla/5.0 (iPad; CPU iPad OS 9_3_6 like Mac OS X) AppleWebKit/534.2 (KHTML, like Gecko) CriOS/27.0.855.0 Mobile/58M631 Safari/534.2",
    },
    {
        "ACW": "7",
        "ADDR": "186.245.251.226",
        "AGENT_NAME": "Mr. Kyle Miller",
        "CALL_ID": "457.228.0765x8971",
        "CUSTOMER_NAME": "Christopher Garcia",
        "END": "08/05/2020 7:06:08 PM",
        "ID": "3d04b-35911-1052d3",
        "START": "08/05/2020 6:52:06 PM",
        "USER_AGENT": "Mozilla/5.0 (X11; Linux x86_64; rv:1.9.5.20) Gecko/2020-09-07 19:03:14 Firefox/3.8",
    },
]

transformed = [
    {
        "agent_name": "Scott Lopez",
        "call_id": "971-605-3989x98841",
        "customer_name": "Lisa Rosales",
        "duration": 659.0,
        "end_time": "08/02/2020 9:23:25 AM",
        "id": "84ef8-bfede-7972af",
        "metadata": {
            "acw": "7",
            "addr": "20.128.243.133",
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3 "
            "rv:3.0; ar-IL) AppleWebKit/531.8.1 (KHTML, like "
            "Gecko) Version/4.0.1 Safari/531.8.1",
        },
        "start_time": "08/02/2020 9:12:26 AM",
    },
    {
        "agent_name": "Paul Duncan",
        "call_id": "001-634-775-4898x281",
        "customer_name": "Sean Allen",
        "duration": 620.0,
        "end_time": "08/05/2020 5:59:30 PM",
        "id": "aad94-4669d-e72ece",
        "metadata": {
            "acw": "7",
            "addr": "105.0.200.198",
            "user_agent": "Mozilla/5.0 (iPad; CPU iPad OS 9_3_6 like Mac OS "
            "X) AppleWebKit/534.2 (KHTML, like Gecko) "
            "CriOS/27.0.855.0 Mobile/58M631 Safari/534.2",
        },
        "start_time": "08/05/2020 5:49:10 PM",
    },
    {
        "agent_name": "Mr. Kyle Miller",
        "call_id": "457.228.0765x8971",
        "customer_name": "Christopher Garcia",
        "duration": 842.0,
        "end_time": "08/05/2020 7:06:08 PM",
        "id": "3d04b-35911-1052d3",
        "metadata": {
            "acw": "7",
            "addr": "186.245.251.226",
            "user_agent": "Mozilla/5.0 (X11; Linux x86_64; rv:1.9.5.20) Gecko/2020-09-07 19:03:14 Firefox/3.8",
        },
        "start_time": "08/05/2020 6:52:06 PM",
    },
]
