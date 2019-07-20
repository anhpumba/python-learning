# Một con ngựa đau cả tàu bỏ cỏ. Kiểm tra trong một tàu ngựa, nếu có một con bị đau
# thì in ra kết quả "Cả tàu bỏ cỏ" còn không thì in ra "Cả tàu ăn cỏ".
# Tàu ngựa là list các con ngựa,
# Mỗi con ngựa, có tên, tình trạng sức khỏe, giới tính

# Solution 01
horses = {
    0: {"Name": "Horse_01", "Healthy Status": "Good", "Gender": "M"},
    1: {"Name": "Horse_02", "Healthy Status": "Good", "Gender": "F"},
    2: {"Name": "Horse_03", "Healthy Status": "Bad", "Gender": "M"}
}

good_message = "Cả tàu ăn cỏ"
bad_message = "Cả tàu bỏ cỏ"
has_horse_bad_healthy = False

for k in horses:
    if horses[k]["Healthy Status"] == "Bad":
        print(f"Found horse with name {horses[k]['Name']} with Healthy Status is {horses[k]['Healthy Status']}"
              f", then result is: {bad_message}")
        has_horse_bad_healthy = True
        break

if not has_horse_bad_healthy:
    print(good_message)

# Solution 02

horses_info = {
    "201907201155": {"Name": "01", "Sex": "M"},
    "201907201156": {"Name": "02", "Sex": "F"},
    "201907201157": {"Name": "03", "Sex": "M"}
}

horses_healthy_status = {
    "201907201155": "Good",
    "201907201156": "Bad",
    "201907201157": "Good"
}

print(bad_message) if "Bad" in horses_healthy_status else print(good_message)

# Solution 03
try:
    print(f"Horse{horses_info[dict((v, k) for k, v in horses_healthy_status.items())['Bad']]['Name']}"
          f"has not good healthy,"
          f"that's why: {bad_message}")
except KeyError:
    print(good_message)

