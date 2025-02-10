def TakimKimyasi(skill):

    skill.sort()
    sonuc = 0

    i = 0
    j = len(skill) - 1

    kontrol = skill[i] + skill[j]
    while i < len(skill)/2:

        if skill[i] + skill[j] == kontrol:
            sonuc += skill[i] * skill[j]
            i += 1
            j -= 1

        else:

            return -1

    return sonuc









