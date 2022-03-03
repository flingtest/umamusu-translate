from os import path
import common
import csv

args = common.Args().parse()
if args.getArg("-h"):
    common.usage("-n <db-translate uma-name.csv> [-src <file to process>]")
NAMES_FILE = args.getArg("-n", False)
TARGET_FILE = args.getArg("-src", False)
TARGET_TYPE = args.getArg("-t", "story").lower()
TARGET_GROUP = args.getArg("-g", False)
TARGET_ID = args.getArg("-id", False)


def createDict():
    global NAMES_FILE
    if not NAMES_FILE:
        NAMES_FILE = "../umamusume-db-translate/src/data/uma-name.csv"
        if not path.exists(NAMES_FILE):
            raise FileNotFoundError("You must specify the uma-name.csv file.")
        print(f"Using auto-found names file {path.realpath(NAMES_FILE)}")
    names = dict()
    with open(NAMES_FILE, "r", newline='', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            names[row[0]] = row[1]

    # a few extras. misc.csv doesn't provide everything
    # todo: probably use an external file?
    names['駿川たづな'] = "Hayakawa Tazuna"
    names['秋川理事長'] = "Chairwoman Akikawa"
    names['樫本代理'] = "Acting Chair Kashimoto"
    # names['モノローグ'] = "Monologue"
    names['記者'] = "Reporter"
    names['記者A'] = "Reporter A"
    names['記者B'] = "Reporter B"
    names['記者C'] = "Reporter C"
    names['記者たち'] = "Reporters"
    names['インタビュアー'] = "Interviewer"
    names['インタビューアーA'] = "Interviewer A"
    names['インタビューアーB'] = "Interviewer B"
    names['ウマ娘'] = "Horsegirl"
    names['ウマ娘A'] = "Horsegirl A"
    names['ウマ娘Ａ'] = "Horsegirl A"
    names['ウマ娘B'] = "Horsegirl B"
    names['ウマ娘C'] = "Horsegirl C"
    names['後輩のウマ娘A'] = "Junior Horsegirl A"
    names['後輩のウマ娘B'] = "Junior Horsegirl B"
    names['後輩ウマ娘A'] = "Junior Horsegirl A"
    names['後輩ウマ娘B'] = "Junior Horsegirl B"
    names['後輩ウマ娘たち'] = "Junior Horsegirls"
    names['同級ウマ娘'] = "Classmate Horsegirl"
    names['先輩ウマ娘'] = "Senior Horsegirl"
    names['同期のウマ娘'] = "Contemporary Horsegirl"
    names['そばかす顔のウマ娘'] = "Freckled Horsegirl"
    names['地元ウマ娘'] = "Local Horsegirl"
    names['どこか上品なウマ娘'] = "Somewhat Refined Horsegirl"
    names['元気なウマ娘の少女'] = "Energetic Horsegirl"
    names['気弱なウマ娘'] = "Timid Horsegirl"
    names['真面目なウマ娘'] = "Serious Horsegirl"
    names['スーツのウマ娘'] = "Horsegirl in a Suit"
    names['ワンピースのウマ娘'] = "Horsegirl in a Dress"
    names['幼いウマ娘'] = "Young Horsegirl"
    names['黒髪のウマ娘'] = "Black-haired Horsegirl"
    names['ロングヘアのウマ娘'] = "Long-haired Horsegirl"
    names['風紀委員のウマ娘'] = "Disciplinary Committee Horsegirl"
    names['図書委員のウマ娘A'] = "Librarian Horsegirl A"
    names['図書委員のウマ娘B'] = "Librarian Horsegirl B"
    names['通りすがりのウマ娘A'] = "Horsegirl Passerby A"
    names['通りすがりのウマ娘B'] = "Horsegirl Passerby B"
    names['観客のウマ娘A'] = "Spectator Horsegirl A"
    names['観客のウマ娘B'] = "Spectator Horsegirl B"
    names['相手のウマ娘A'] = "Opponent Horsegirl A"
    names['相手のウマ娘B'] = "Opponent Horsegirl B"
    names['読手のウマ娘'] = "Reader Horsegirl" #They might bring this back later now that umakaruta exists?
    names['美浦寮のウマ娘'] = "Miho Dorm Horsegirl"
    names['栗東寮のウマ娘'] = "Rittou Dorm Horsegirl"
    names['合宿中のウマ娘A'] = "Fellow Camp Horsegirl A"
    names['合宿中のウマ娘B'] = "Fellow Camp Horsegirl B"
    names['気弱そうなウマ娘'] = "Timid-looking Horsegirl"
    names['素直なウマ娘'] = "Honest Horsegirl"
    names['前髪ぱっつんのウマ娘'] = "Horsegirl with Straight-cut Bangs"
    names['タレ目のウマ娘'] = "Droopy-eyed Horsegirl"
    names['黒髪ボブのウマ娘'] = "Horsegirl with Black Bob-cut"
    names['ウマ娘の母親'] = "Horsegirl's Mom"
    names['ウマ娘たち'] = "Horsegirls"
    names['？？？'] = "???"
    names['ニュースキャスター'] = "Newscaster"
    names['ウマ娘ファンA'] = "Horsegirl Fan A"
    names['ウマ娘ファンB'] = "Horsegirl Fan B"
    names['教師'] = "Teacher"
    names['先生'] = "Teacher"
    names['先生A'] = "Teacher A"
    names['生徒たち'] = "Teachers"
    names['教官'] = "Instructor"
    names['教官A'] = "Instructor A"
    names['図書委員'] = "Librarian"
    names['スタッフ'] = "Staff"
    names['スタッフA'] = "Staff A"
    names['スタッフＡ'] = "Staff A"
    names['スタッフB'] = "Staff B"
    names['スタッフＢ'] = "Staff B"
    names['スタッフC'] = "Staff C"
    names['スタッフＣ'] = "Staff C"
    names['調理スタッフ'] = "Cooking Staff"
    names['学園スタッフ'] = "Academy Staff"
    names['学園スタッフA'] = "Academy Staff A"
    names['感謝祭実行委員A'] = "FanFes Committee Member A"
    names['感謝祭実行委員B'] = "FanFes Committee Member B"
    names['観客A'] = "Spectator A"
    names['観客B'] = "Spectator B"
    names['観客C'] = "Spectator C"
    names['観客D'] = "Spectator D"
    names['観客E'] = "Spectator E"
    names['観客F'] = "Spectator F"
    names['観客G'] = "Spectator G"
    names['女性の観客A'] = "Spectator Woman A"
    names['女性の観客B'] = "Spectator Woman B"
    names['男性の観客A'] = "Spectator Man A"
    names['男性の観客B'] = "Spectator Man B"
    names['観客たち'] = "Crowd"
    names['観客'] = "Crowd"
    names['歓声'] = "Cheers"
    names['大歓声'] = "Loud Cheers"
    names['実況'] = "Broadcast"
    names['イベント実況'] = "Event Broadcast"
    names['審査員'] = "Judge"
    names['テレビ'] = "TV"
    names['テレビの音'] = "TV Report"
    names['手紙'] = "Letter"
    names['新人トレーナー'] = "Rookie Trainer"
    names['新人トレーナーA'] = "Rookie Trainer A"
    names['新人トレーナーＡ'] = "Rookie Trainer A"
    names['新人トレーナーB'] = "Rookie Trainer B"
    names['新人トレーナーＢ'] = "Rookie Trainer B"
    names['中堅トレーナー'] = "Average Trainer"
    names['中堅トレーナーA'] = "Average Trainer A"
    names['中堅トレーナーＡ'] = "Average Trainer A"
    names['中堅トレーナーB'] = "Average Trainer B"
    names['中堅トレーナーＢ'] = "Average Trainer B"
    names['ベテラントレーナー'] = "Veteran Trainer"
    names['ベテラントレーナーA'] = "Veteran Trainer A"
    names['ベテラントレーナーＡ'] = "Veteran Trainer A"
    names['ベテラントレーナーB'] = "Veteran Trainer B"
    names['ベテラントレーナーＢ'] = "Veteran Trainer B"
    names['先代トレーナー'] = "Chief Trainer"
    names['トレーナーたち'] = "Trainers"
    names['男性'] = "Man"
    names['男性Ａ'] = "Man A"
    names['女性'] = "Woman"
    names['女性Ａ'] = "Woman A"
    names['女性Ｂ'] = "Woman B"
    names['女の子'] = "Girl"
    names['女の子A'] = "Girl A"
    names['少女'] = "Young Girl"
    names['男の子'] = "Boy"
    names['男の子A'] = "Boy A"
    names['男の子B'] = "Boy B"
    names['ファン'] = "Fan"
    names['ファンの男性'] = "Male Fan"
    names['ファンの女性'] = "Female Fan"
    names['ファンたち'] = "Fans"
    names['司会者'] = "Host"
    names['司会者A'] = "Host A"
    names['テレビ番組の司会'] = "TV Host"
    names['クラスメイト'] = "Classmate"
    names['クラスメイトA'] = "Classmate A"
    names['クラスメイトＡ'] = "Classmate A"
    names['クラスメイトB'] = "Classmate B"
    names['クラスメイトＢ'] = "Classmate B"
    names['クラスメイトC'] = "Classmate C"
    names['クラスメイトＣ'] = "Classmate C"
    names['クラスメイトD'] = "Classmate D"
    names['クラスメイトＤ'] = "Classmate D"
    names['クラスメイトたち'] = "Classmates"
    names['陽気なクラスメイト'] = "Cheerful Classmate"
    names['優しいクラスメイト'] = "Gentle Classmate"
    names['爽やかなウマ娘'] = "Lively Classmate"
    names['商店街の人'] = "Market Person"
    names['商店街の人A'] = "Market Person A"
    names['商店街の人B'] = "Market Person B"
    names['商店街の人たち'] = "Market People"
    names['遊園地のスタッフ'] = "Amusement Park Staff"
    names['呼び込みの男性'] = "Male Barker"
    names['カフェ店員'] = "Cafe Employee"
    names['カフェの店員'] = "Cafe Employee"
    names['カフェのスタッフ'] = "Cafe Staff"
    names['屋台の店主'] = "Stallkeeper"
    names['屋台のおばさん'] = "Elder Stallkeeper Lady"
    names['八百屋のおばあさん'] = "Elder Greengrocer Lady"
    names['店主'] = "Shopkeeper"
    names['店員'] = "Shop Assistant"
    names['店員A'] = "Shop Assistant A"
    names['お店のスタッフA'] = "Shop Staff A"
    names['お店のスタッフB'] = "Shop Staff B"
    names['男性客'] = "Male Customer"
    names['女性客'] = "Female Customer"
    names['常連客'] = "Regular Customer"
    names['客たち'] = "Customers"
    names['母親'] = "Mother"
    names['父親'] = "Father"
    names['子ども'] = "Child"
    names['子どもA'] = "Child A"
    names['子どもたち'] = "Children"
    names['子供たち'] = "Children"
    names['男の子たち'] = "Male Child"
    names['ファンの子ども'] = "Fan's Child"
    names['ファンの子'] = "Child Fan"
    names['ファンの子どもたち'] = "Fan's Children"
    names['ウマ娘の子どもたち'] = "Horsegirl Children"
    names['おばさん'] = "Elder Lady"
    names['おばさんA'] = "Elder Lady A"
    names['おばさんB'] = "Elder Lady B"
    names['おじいさん'] = "Elder Man"
    names['広報委員長'] = "PR Committee Chair"
    names['広報委員'] = "PR Committee Member"
    names['風紀委員たち'] = "PM Committee Member"
    names['宇宙人'] = "Alien"
    names['2人'] = "Both"
    names['3人'] = "All 3"
    names['4人'] = "All 4"
    names['みんな'] = "Everyone"
    names['通行人A'] = "Passerby A"
    names['通行人B'] = "Passerby B"
    names['通行人たち'] = "Passersby"
    names['カメラマンA'] = "Cameraman A"
    names['カメラマンB'] = "Cameraman B"
    names['整備士A'] = "Mechanic A"
    names['整備士Ａ'] = "Mechanic A"
    names['整備士B'] = "Mechanic B"
    names['整備士Ｂ'] = "Mechanic B"
    names['整備スタッフ'] = "Maintenance Staff"
    names['船乗り'] = "Sailor"
    names['SP隊長'] = "SP Commander"
    names['女優'] = "Actress"
    names['ネコ'] = "Cat"
    names['野良ネコ'] = "Stray Cat"
    names['イヌ'] = "Dog"
    names['ドラゴン'] = "Dragon"
    names['牛'] = "Cow"
    names['カラス'] = "Crow"
    names['カモ'] = "Duck"
    names['キャロットマン'] = "Carrot Man"
    names['ビューティー安心沢'] = "Beauty Anshinzawa"
    names['スズカのトレーナー'] = "Suzuka's Trainer"
    names['フラッシュの父親'] = "Flash' Father"
    names['親戚'] = "Relative"
    names['主婦'] = "Housewive"
    names['射的屋'] = "Shooting Gallery"
    return names

def translate(namesDict):
    if TARGET_FILE: files = [TARGET_FILE]
    else: files = common.searchFiles(TARGET_TYPE, TARGET_GROUP, TARGET_ID)

    for file in files:
        file = common.TranslationFile(file)
        for block in file.getTextBlocks():
            name = block['jpName']
            if name and name in namesDict:
                block['enName'] = namesDict[name]
        file.save()

def main():
    dict = createDict()
    translate(dict)
    # print(file.data)
    # file.save()

main()