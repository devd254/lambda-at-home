# Select execution environment (if warm one exists that is sitting idle, use that one. cold start)
# cold starts will simply choose first non-active environment (runner)
# cold starts add an extra 10 seconds simulated time (with time.sleep)
# return the selected runner after it's been started up
def start():
    pass