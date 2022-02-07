def email_grabber(website: str):
    import requests
    # sending the request with fake headers so your not blocked
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                             "(KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"}
    r = requests.get(website, headers=headers)
    r = r.text
    r = str(r)
    email_found = 0
    # looking for Email
    for index, m in enumerate(r):
        if m == "m":
            a_at_low = int(index)
            a_at_high = int(index + 6)
            possible_mailto = r[a_at_low:a_at_high]
            if possible_mailto == "mailto":
                mailto = r[a_at_low:a_at_high + 30]
                for indexy, lines in enumerate(mailto):
                    if lines == "\"":
                        email_start = 7
                        email_end = indexy
                        email = mailto[email_start:email_end]
                        email_found = 1
                        print(email)
            else:
                continue
    if email_found == 0:
        print("No emails found")
