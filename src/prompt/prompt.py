def prompt():
    from src.data.dataRunner import getUserData, buildData
    from src.prompt.inputCases import mainCase
    import colorama
    import sys

    print("Maverick 0.0.2")
    print("Loading...")

    # loading start

    # buildData()
    userdata = getUserData()

    colorama.init() # init colorama for all system files

    sys.path.append("../Maverick") # make path include all directories

    # loading end

    print()

    while True:

        user_input = input("#> ")

        mainCase(user_input,userdata["programs"])