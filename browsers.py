from pywinauto import Application

def ff_urls():
    urls = []
    try:
        firefox = Application(backend="uia").connect(title_re='.*Firefox.*')
    except:
        print(r"<font color='Red'>[music-dl] ERROR: Firefox is not running</font>")
        return urls
    wd = firefox.windows()[0]
    tabs = wd.children()
    for tab in tabs:
        try:
            s = tab.children()[0].children()[0]
            url = s.legacy_properties()["Value"]
            urls.append(url)
        except:
            pass
    return urls

def ch_urls():
    print("Not supported yet")
    return []

    """
    try:
        chrome = Application(backend="uia").connect(title_re='.*Chrome.*', found_index=0, timeout=5)
    except:
        chrome = None
        print("[music-dl] ERROR: Chrome is not running")
        return []
    """