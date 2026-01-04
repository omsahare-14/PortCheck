def classify_exposure(address):
    if address in ("127.0.0.1", "::1"):
        return "local"
    return "exposed"