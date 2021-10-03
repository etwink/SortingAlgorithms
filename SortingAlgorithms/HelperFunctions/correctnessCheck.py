def correctnessCheck(l):
    for i in range(1, len(l)):
        if l[i-1] != l[i] - 1:
            return False
    return True