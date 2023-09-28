def wait():
    i = 0
    while i == 0:
        print("                                            ok : enter")
        i = input()

def line(x):
    if x == 0:
        print("=======================================================")
    elif x == 1:
        print("* * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    elif x == 2:
        print("~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~")
    elif x == 3:
        print("+ + + + + + + + + + + + + + + + + + + + + + + + + + + +")
    elif x == 4:
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    else:
        print("  ")

def sakuzyo(x):
    if "_" in(str(x)):
        x = x.replace("_", "")

    return x

line(4)
line(9)
line(1)
print("このプログラムは、SXmeisterで作成されたnetリストを")
print("オペアンプコンテストの形式に対応した形に変換するプログラムです")
line(1)
wait()

line(0)
print("Sxmeisterのnetリストを変換していきます")
print("Sxmeisterで作成したネットリストの名前を記入してください")
yomifile = input()
line(2)

f = open(yomifile, 'r')

yomi = ["yomi"]

while True:
    x = f.readline()
    yomi.append(x)
    if x == '':
        break

f.close()

print("            ", yomifile,"という名前のファイルを読み込みました。")
line(0)
wait()


line(0)
print("電源電圧(VSS-VDD間の電圧)を入力してください。")
Vpp = input()
line(3)
print("            電源電圧を", Vpp, "[V]と設定しました")

line(2)
print("非反転入力（in+）のネット名を入力してください。")
inp = input()
inp = sakuzyo(inp)
line(3)
print("            非反転入力（in+）を", inp, "と設定しました")

line(2)
print("反転入力（in-）のネット名を入力してください。")
inm = input()
inm = sakuzyo(inm)
line(3)
print("            反転入力(in-)を", inm, "と設定しました")

line(2)
print("出力(Vout)のネット名を入力してください。")
out = input()
out = sakuzyo(out)
line(3)
print("            出力(Vout)を", out, "と設定しました")

line(2)
print("正電源（VDD）のネット名を入力してください。")
VDD = input()
line(3)
print("            正電源(VDD)を", VDD, "と設定しました")

line(2)
print("負電源（VSS）のネット名を入力してください。")
VSS = input()
line(3)
print("            負電源(VSS)を", VSS, "と設定しました")
line(0)
wait()
line(0)
print("次にオペアンプコンテスト用のnetリストを作成します")
print("提出回路の名前を記入してください")
kakifile = input()
line(3)
print("            ", kakifile, ".net というネットリストを作成します。")
line(0)
wait()


line(0)
f = open(kakifile +'.net', 'w')
f.write("opamp_netlist\n")
f.write(".param psvoltage=" + Vpp + "\n")
f.write(".subckt opamp " + inm + " " + inp + " " + out + " VDD VSS \n")
for w in yomi:

    w = sakuzyo(w)
    if VDD in (str(w)):
        w = w.replace(VDD, "VDD")
    if VSS in (str(w)):
        w = w.replace(VSS, "VSS")

    if "*" in (str(w)):
        print(w)
    elif ".GLOBAL" in(str(w)):
        print(w)
    elif ".SUBCKT" in(str(w)):
        print(w)
    elif ".END" in(str(w)):
        print(w)
    elif "yomi" in (str(w)):
        print("削除した文")
    elif ".end" in (str(w)):
        print(w)
    elif "V0" in(str(w)) or "V1" in (str(w)) or "V2" in (str(w)) or "V3" in (str(w)) or "V4" in (str(w)) or "V5" in (str(w)):
        print(w)
    elif "V6" in (str(w)) or "V7" in (str(w)) or "V8" in (str(w)) or "V9" in (str(w)) or "V10" in (str(w)):
        print(w)
    elif "bsim3v3" in(str(w)):
        w = w.replace("bsim3v3", "cmos")
        f.write(str(w))
    else:
        f.write(str(w))

f.write(".ends opamp")

f.close()

line(3)
print("netリスト作成完了です")
line(0)


line(1)
print("              お疲れさまでした")
line(1)
wait()