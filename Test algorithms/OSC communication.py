from pythonosc import udp_client

######### format the approximation set and send it over to SonOpt via OSC #######
    approximation_set = algorithm.result().F
    obj_one = ['{:f}'.format(item) for item in approximation_set[:, 0]]
    obj_two = ['{:f}'.format(item) for item in approximation_set[:, 1]]
    objs_combined = [obj_one, obj_two]
    formatted_approximation_set = [' '.join(str(item) for item in column) for column in zip(*objs_combined)]
    client_a = udp_client.SimpleUDPClient("127.0.0.1", 5002)
    client_a.send_message("start", formatted_approximation_set)
    sleep(0.3)
    ################
