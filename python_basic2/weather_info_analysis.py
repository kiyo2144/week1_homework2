def average_temperature(weather_information):
    total = 0
    for info in weather_information:
        total += info["temperature"]
    return total / len(weather_information)
    # pass


def station_names_by_prefecture(weather_information, prefecture):
    stations = []
    for info in weather_information:
        if info["prefecture"] == prefecture:
            stations.append(info["station"])
    return ",".join(stations)
    # pass


def average_temperature_by_prefecture(weather_information, prefecture):
    temperatures = []
    for info in weather_information:
        if info["prefecture"] == prefecture:
            temperatures.append(info["temperature"])
    return sum(temperatures) / len(temperatures)
    # pass


def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    print(round(average_temperature(weather_information), 1))

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    print(station_names_by_prefecture(weather_information, "大阪府"))  # 梅田,大阪,堺

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    print(round(average_temperature_by_prefecture(weather_information, "福岡県"), 1))


if __name__ == "__main__":
    main()
