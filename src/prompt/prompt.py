def prompt():
    from src.data.dataRunner import getUserData, buildData
    from src.prompt.inputCases import mainCase
    from progress.bar import IncrementalBar
    import colorama
    import sys

    print("Maverick 0.0.2")

    # loading start

    loaderBar = IncrementalBar("Loading...",max=6)

    buildData()

    loaderBar.next() ####################

    userdata = getUserData()

    loaderBar.next() ####################

    programs = userdata["programs"]

    loaderBar.next() ####################

    userdata.close()

    loaderBar.next() ####################

    colorama.init() # init colorama for all system files

    loaderBar.next() ####################

    sys.path.append("../Maverick") # make path include all directories

    loaderBar.next() ####################

    # loading end

    print()

    while True:

        user_input = input("#> ")

        mainCase(user_input,programs)