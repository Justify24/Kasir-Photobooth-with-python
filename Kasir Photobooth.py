import tempfile
from tkinter import *
from tkinter import messagebox
import random, os,sys

#fungsi python
kodepembayaran = random.randint(500, 1000)

if not os.path.exists('Daftar Transaksi'):
    os.mkdir('Daftar Transaksi')

#pengolahan hasil
def total():
    singlebasic = int(singlebasicEntry.get()) * 40000
    couplebasic = int(couplebasicEntry.get()) * 65000
    groupbasic = int(groupbasicEntry.get()) * 150000
    singlepremium = int(singlepremiumEntry.get()) * 60000
    couplepremium = int(couplepremiumEntry.get()) * 85000
    grouppremium = int(grouppremiumEntry.get()) * 200000

    total_harga_paket = singlebasic + couplebasic + groupbasic + singlepremium + couplepremium + grouppremium
    totalhargapaketEntry.delete(0, END)  # Menghapus nilai sebelumnya
    totalhargapaketEntry.insert(0, total_harga_paket)

    addtime=int(addtimeEntry.get())*15000
    addprintfoto=int(addprintfotoEntry.get())*10000
    addperson=int(addpersonEntry.get())*20000

    total_harga_additional = addtime + addprintfoto + addperson
    totalhargaadditionalEntry.delete(0, END)  # Menghapus nilai sebelumnya
    totalhargaadditionalEntry.insert(0, total_harga_additional)

    aksesorisbando=int(aksesorisbandoEntry.get())*1000
    aksesorisbungapalsu=int(aksesorisbungapalsuEntry.get())*2000
    aksesorislatar=int(aksesorislatarEntry.get())*1000
    aksesorisboneka=int(aksesorisbonekaEntry.get())*2000
    aksesoriskacamata=int(aksesoriskacamataEntry.get())*1000
    aksesorispedang=int(aksesorispedangEntry.get())*1000
    aksesorisperisai=int(aksesorisperisaiEntry.get())*1000
    aksesorispakaiankustom=int(aksesorispakaiankustomEntry.get())*50000
    aksesorisdasi=int(aksesorisdasiEntry.get())*2000

    total_harga_aksesoris = aksesorisbando + aksesorisbungapalsu + aksesorislatar + aksesorisboneka + aksesoriskacamata + aksesorispedang + aksesorisperisai + aksesorispakaiankustom + aksesorisdasi
    totalhargaaksesorisEntry.delete(0, END)  # Menghapus nilai sebelumnya
    totalhargaaksesorisEntry.insert(0, total_harga_aksesoris)

    total_harga1 = total_harga_paket + total_harga_additional + total_harga_aksesoris

    total_pajak = total_harga1 * 0.09
    totalpajakEntry.delete(0, END)  # Menghapus nilai sebelumnya
    totalpajakEntry.insert(0, total_pajak)

    total_harga =total_harga1 + total_pajak
    totaltransaksiEntry.delete(0, END)  # Menghapus nilai sebelumnya
    totaltransaksiEntry.insert(0, total_harga)

    total_bayar = 0
    totalbayarEntry.delete(0, END)  # Menghapus nilai sebelumnya
    totalbayarEntry.insert(0, total_bayar)

def bayar():

    #paketfoto
    singlebasic = int(singlebasicEntry.get()) * 40000
    couplebasic = int(couplebasicEntry.get()) * 65000
    groupbasic = int(groupbasicEntry.get()) * 150000
    singlepremium = int(singlepremiumEntry.get()) * 60000
    couplepremium = int(couplepremiumEntry.get()) * 85000
    grouppremium = int(grouppremiumEntry.get()) * 200000

    #Produk Additional
    addtime = int(addtimeEntry.get()) * 15000
    addprintfoto = int(addprintfotoEntry.get()) * 10000
    addperson = int(addpersonEntry.get()) * 20000

    #Produk Sewa
    aksesorisbando=int(aksesorisbandoEntry.get())*1000
    aksesorisbungapalsu=int(aksesorisbungapalsuEntry.get())*2000
    aksesorislatar=int(aksesorislatarEntry.get())*1000
    aksesorisboneka=int(aksesorisbonekaEntry.get())*2000
    aksesoriskacamata=int(aksesoriskacamataEntry.get())*1000
    aksesorispedang=int(aksesorispedangEntry.get())*1000
    aksesorisperisai=int(aksesorisperisaiEntry.get())*1000
    aksesorispakaiankustom=int(aksesorispakaiankustomEntry.get())*50000
    aksesorisdasi=int(aksesorisdasiEntry.get())*2000

    total_harga_paket = singlebasic + couplebasic + groupbasic + singlepremium + couplepremium + grouppremium
    totalhargapaketEntry.delete(0, END)  # Menghapus nilai sebelumnya
    totalhargapaketEntry.insert(0, total_harga_paket)

    total_harga_additional = addtime + addprintfoto + addperson
    totalhargaadditionalEntry.delete(0, END)  # Menghapus nilai sebelumnya
    totalhargaadditionalEntry.insert(0, total_harga_additional)

    total_harga_aksesoris = aksesorisbando + aksesorisbungapalsu + aksesorislatar + aksesorisboneka + aksesoriskacamata + aksesorispedang + aksesorisperisai + aksesorispakaiankustom + aksesorisdasi
    totalhargaaksesorisEntry.delete(0, END)  # Menghapus nilai sebelumnya
    totalhargaaksesorisEntry.insert(0, total_harga_aksesoris)

    total_harga1 = total_harga_paket + total_harga_additional + total_harga_aksesoris

    total_pajak = total_harga1 * 0.09
    totalpajakEntry.delete(0, END)  # Menghapus nilai sebelumnya
    totalpajakEntry.insert(0, total_pajak)

    total_harga =total_harga1 + total_pajak
    totaltransaksiEntry.delete(0, END)  # Menghapus nilai sebelumnya
    totaltransaksiEntry.insert(0, total_harga)

    total_bayar = float(totalbayarEntry.get())
    totalbayarEntry.delete(0, END)  # Menghapus nilai sebelumnya
    totalbayarEntry.insert(0, total_bayar)

    total_kembalian = total_bayar - total_harga
    totalkembalianEntry.delete(0, END)  # Menghapus nilai sebelumnya
    totalkembalianEntry.insert(0, total_kembalian)

    if namaEntry.get=='' or nomorhpEntry.get()=='':
        messagebox.showerror('Error', 'Mohon diisi data Customer')
    elif totalhargapaketEntry.get()=='' or totalhargaadditionalEntry.get()=='' or totalhargaaksesorisEntry.get()=='':
        messagebox.showerror('Error', 'Mohon produknya dipilih')
    elif totalhargapaketEntry.get()=='0':
        messagebox.showerror('Error', 'Mohon untuk dipilih Paketnya terlebih dahulu')
    elif totalbayarEntry.get()=='0.0':
        messagebox.showerror('Error', 'Mohon diisi nominal uang yang diterima')

    else:
        textarea.insert(END, '\t\tSelamat Datang\n')
        textarea.insert(END, f'\nKode Transaksi: {kodepembayaran}')
        textarea.insert(END, f'\nNama Pelanggan: {namaEntry.get()}')
        textarea.insert(END, f'\nNomor HP      : {nomorhpEntry.get()}')
        textarea.insert(END, '\n=========================================')
        textarea.insert(END, '\nProduk\t\tQuantity\t\t  Harga')
        textarea.insert(END, '\n=========================================')

        #Produk paket
        #basic
        if singlebasicEntry.get() !='0':
            textarea.insert(END, f'\nPaket Single\t\t   {singlebasicEntry.get()}\t\t  {singlebasic}\nBasic')
        if couplebasicEntry.get() !='0':
            textarea.insert(END, f'\nPaket Couple\t\t   {couplebasicEntry.get()}\t\t  {couplebasic}\nBasic')
        if groupbasicEntry.get() !='0':
            textarea.insert(END, f'\nPaket Group \t\t   {groupbasicEntry.get()}\t\t  {groupbasic}\nBasic')
        #premium
        if singlepremiumEntry.get() !='0':
            textarea.insert(END, f'\nPaket Single\t\t   {singlepremiumEntry.get()}\t\t  {singlepremium}\nPremium')
        if couplepremiumEntry.get() !='0':
            textarea.insert(END, f'\nPaket Couple\t\t   {couplepremiumEntry.get()}\t\t  {couplepremium}\nPremium')
        if grouppremiumEntry.get() !='0':
            textarea.insert(END, f'\nPaket Group \t\t   {grouppremiumEntry.get()}\t\t  {grouppremium}\nPremium')

        #Produk Additional
        if addtimeEntry.get() !='0':
            textarea.insert(END, f'\nTambah Waktu\t\t   {addtimeEntry.get()}\t\t  {addtime}')
        if addpersonEntry.get() !='0':
            textarea.insert(END, f'\nTambah Orang\t\t   {addpersonEntry.get()}\t\t  {addperson}')
        if addprintfotoEntry.get() !='0':
            textarea.insert(END, f'\nTambah Print\t\t   {addprintfotoEntry.get()}\t\t  {addtime}\nFoto')

        #Produk Sewa
        if aksesorisbandoEntry.get() !='0':
            textarea.insert(END, f'\nSewa Bando\t\t   {aksesorisbandoEntry.get()}\t\t  {aksesorisbando}')
        if aksesorisbungapalsuEntry.get() !='0':
            textarea.insert(END, f'\nSewa Bunga\t\t   {aksesorisbungapalsuEntry.get()}\t\t  {aksesorisbungapalsu}\nPalsu')
        if aksesorislatarEntry.get() !='0':
            textarea.insert(END, f'\nSewa Latar\t\t   {aksesorislatarEntry.get()}\t\t  {aksesorislatar}')
        if aksesorisbonekaEntry.get() !='0':
            textarea.insert(END, f'\nSewa Boneka\t\t   {aksesorisbonekaEntry.get()}\t\t  {aksesorisboneka}')
        if aksesoriskacamataEntry.get() !='0':
            textarea.insert(END, f'\nSewa Kacamata\t\t   {aksesoriskacamataEntry.get()}\t\t  {aksesoriskacamata}')
        if aksesorispedangEntry.get() !='0':
            textarea.insert(END, f'\nSewa Pedang\t\t   {aksesorispedangEntry.get()}\t\t  {aksesorispedang}')
        if aksesorisperisaiEntry.get() !='0':
            textarea.insert(END, f'\nSewa Perisai\t\t   {aksesorisperisaiEntry.get()}\t\t  {aksesorisperisai}')
        if aksesorispakaiankustomEntry.get() !='0':
            textarea.insert(END, f'\nSewa Pakaian\t\t   {aksesorispakaiankustomEntry.get()}\t\t  {aksesorispakaiankustom}\nKustom')
        if aksesorisdasiEntry.get() !='0':
            textarea.insert(END, f'\nSewa Dasi\t\t   {aksesorisdasiEntry.get()}\t\t  {aksesorisdasi}')

        textarea.insert(END, '\n-----------------------------------------')

        if totaltransaksiEntry.get()!='0':
            textarea.insert(END, f'\n Total Transaksi\t\t\t\t{total_pajak}')

        if totalpajakEntry.get()!='0':
            textarea.insert(END, f'\n Pajak (9%)\t\t\t\t{total_pajak}')

        textarea.insert(END, '\n-----------------------------------------')

        if totalbayarEntry.get()!='0':
            textarea.insert(END, f'\n Uang Dibayar\t\t\t\t{total_bayar}')
        if totalkembalianEntry.get()!='0':
            textarea.insert(END, f'\n Uang Kembalian\t\t\t\t{total_kembalian}')

        textarea.insert(END, '\n\n\t\tTerima Kasih')

def simpan():
    global kodepembayaran
    result = messagebox.askyesno('Confirm', 'Apakah datanya sudah benar?')
    if result:
        simpan_content = textarea.get(1.0, END)
        file = open(f'Daftar Transaksi/{kodepembayaran}.txt', 'w')
        file.write(simpan_content)
        file.close()
        messagebox.showinfo('Success', f'{kodepembayaran} sukses tersimpan')
        kodepembayaran = random.randint(500, 1000)


def cari_transaksi():
    nomor_pembayaran = nomorpembayaranEntry.get()
    for i in os.listdir('Daftar Transaksi/'):
        if i.split('.')[0] == nomor_pembayaran:
            file_path = f'Daftar Transaksi/{i}'
            try:
                with open(file_path, 'r') as file:
                    textarea.delete(1.0, END)
                    for data in file:
                        textarea.insert(END, data)
            except FileNotFoundError:
                messagebox.showerror('Error', 'File tidak ditemukan')
            break
    else:
        messagebox.showerror('Error', 'Kode Pembayaran tidak valid')
def print_struk():
    if textarea.get(1.0, END)=='\n':
        messagebox.showerror('Error','Transaksi tidak ada')
    else:
        file=tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0,END))
        os.startfile(file, 'print')

def reset():

    singlebasicEntry.delete(0,END)
    couplebasicEntry.delete(0,END)
    groupbasicEntry.delete(0,END)
    singlepremiumEntry.delete(0,END)
    couplepremiumEntry.delete(0,END)
    grouppremiumEntry.delete(0,END)

    addtimeEntry.delete(0,END)
    addpersonEntry.delete(0,END)
    addprintfotoEntry.delete(0,END)

    aksesorisbandoEntry.delete(0,END)
    aksesorisbungapalsuEntry.delete(0,END)
    aksesorislatarEntry.delete(0,END)
    aksesorisbonekaEntry.delete(0,END)
    aksesoriskacamataEntry.delete(0,END)
    aksesorispedangEntry.delete(0,END)
    aksesorisperisaiEntry.delete(0,END)
    aksesorispakaiankustomEntry.delete(0,END)
    aksesorisdasiEntry.delete(0,END)

    singlebasicEntry.insert(0, 0)
    couplebasicEntry.insert(0, 0)
    groupbasicEntry.insert(0, 0)
    singlepremiumEntry.insert(0, 0)
    couplepremiumEntry.insert(0, 0)
    grouppremiumEntry.insert(0, 0)

    addtimeEntry.insert(0, 0)
    addpersonEntry.insert(0, 0)
    addprintfotoEntry.insert(0, 0)

    aksesorisbandoEntry.insert(0, 0)
    aksesorisbungapalsuEntry.insert(0, 0)
    aksesorislatarEntry.insert(0, 0)
    aksesorisbonekaEntry.insert(0, 0)
    aksesoriskacamataEntry.insert(0, 0)
    aksesorispedangEntry.insert(0, 0)
    aksesorisperisaiEntry.insert(0, 0)
    aksesorispakaiankustomEntry.insert(0, 0)
    aksesorisdasiEntry.insert(0, 0)

    totalhargapaketEntry.delete(0,END)
    totalhargaadditionalEntry.delete(0,END)
    totalhargaaksesorisEntry.delete(0,END)

    totalpajakEntry.delete(0,END)
    totaltransaksiEntry.delete(0,END)

    totalbayarEntry.delete(0,END)
    totalkembalianEntry.delete(0,END)

    namaEntry.delete(0, END)
    nomorhpEntry.delete(0, END)
    nomorpembayaranEntry.delete(0, END)

    textarea.delete(1.0, END)

def keluar():
    result = messagebox.askyesno('Konfirmasi', 'Apakah Anda yakin ingin keluar?')
    if result:
        # Keluar dari program
        sys.exit(0)

#####################################################################################################################################

root=Tk()
root.title('Kasir PhotoBooth')
root.geometry('1280x768')
#root.iconbitmap('icon.ico')

#HEADING
headingLabel=Label(root,text='Kasir PhotoBooth',font=('times new roman',30,'bold')
                   ,bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

#FRAME1
pelanggan_detail_frame=LabelFrame(root, text='Data pelanggan', font=('times new roman',15,'bold'),
                fg='gold',bd=8,relief=GROOVE,bg='gray20')
pelanggan_detail_frame.pack(fill=X)

#nama
namaLabel=Label(pelanggan_detail_frame, text='Nama',font=('times new roman',15,'bold'),bg='gray20',
                fg='white')
namaLabel.grid(row=0,column=0,padx=20)

#EntryNama
namaEntry=Entry(pelanggan_detail_frame,font=('arial',15),bd=7,width=18)
namaEntry.grid(row=0,column=1,padx=8)

#nomorHp
nomorhpLabel=Label(pelanggan_detail_frame, text='Nomor HP',font=('times new roman',15,'bold'),bg='gray20',
                fg='white')
nomorhpLabel.grid(row=0,column=2,padx=20,pady=2)

#EntryNomorHP
nomorhpEntry=Entry(pelanggan_detail_frame,font=('arial',15),bd=7,width=18)
nomorhpEntry.grid(row=0,column=3,padx=8)

#kodepembayaran
nomorpembayaranLabel=Label(pelanggan_detail_frame, text='Kode Pembayaran',font=('times new roman',15,'bold'),bg='gray20',
                fg='white')
nomorpembayaranLabel.grid(row=0,column=4,padx=20,pady=2)

#Entrykodepembayaran
nomorpembayaranEntry=Entry(pelanggan_detail_frame,font=('arial',15),bd=7,width=18)
nomorpembayaranEntry.grid(row=0,column=5,padx=8)

#buttoncari
searchButton=Button(pelanggan_detail_frame, text='CARI',font=('arial',12,'bold'),bd=7,width=10,command=cari_transaksi)
searchButton.grid(row=0, column=6,padx=20,pady=8)


#frameproduk
productsFrame=Frame()
productsFrame.pack()

#frame paket Foto
paketFrame = LabelFrame(productsFrame, text='Paket Foto', font=('arial', 15, 'bold'),
                        fg='gold', bd=8, relief=GROOVE, bg='gray20')

paketFrame.grid(row=0,column=0)

# Keterangan Label Single
basicLabel = Label(paketFrame, text='Basic', font=('arial', 15, 'bold'),
                   bg='gray20', fg='gold')
basicLabel.grid(row=1, column=0)

# labelsinglebasic
singlebasicLabel = Label(paketFrame, text='Single Basic', font=('times new roman', 15, 'bold'),
                         bg='gray20', fg='white')
singlebasicLabel.grid(row=2, column=0, pady=7, padx=10)

# entrysinglebasic
singlebasicEntry = Entry(paketFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
singlebasicEntry.grid(row=2, column=1, pady=7, padx=10)
singlebasicEntry.insert(0,0)

# labelcouplebasic
couplebasicLabel = Label(paketFrame, text='Couple Basic', font=('times new roman', 15, 'bold'),
                         bg='gray20', fg='white')
couplebasicLabel.grid(row=3, column=0, pady=7, padx=10)

# entrycouplebasic
couplebasicEntry = Entry(paketFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
couplebasicEntry.grid(row=3, column=1, pady=7, padx=10)
couplebasicEntry.insert(0,0)


# labelgroupbasic
groupbasicLabel = Label(paketFrame, text='Group Basic', font=('times new roman', 15, 'bold'),
                        bg='gray20', fg='white')
groupbasicLabel.grid(row=4, column=0, pady=7, padx=10)

# entrygroupbasic
groupbasicEntry = Entry(paketFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
groupbasicEntry.grid(row=4, column=1, pady=7, padx=10)
groupbasicEntry.insert(0,0)

# Keterangan Label Premium
premiumLabel = Label(paketFrame, text='Premium', font=('arial', 15, 'bold'),
                     bg='gray20', fg='gold')
premiumLabel.grid(row=5, column=0)

# labelsinglepremium
singlepremiumLabel = Label(paketFrame, text='Single Premium', font=('times new roman', 15, 'bold'),
                           bg='gray20', fg='white')
singlepremiumLabel.grid(row=6, column=0, pady=7, padx=10)

# entrysinglepremium
singlepremiumEntry = Entry(paketFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
singlepremiumEntry.grid(row=6, column=1, pady=7, padx=10)
singlepremiumEntry.insert(0,0)

# labelcouplepremium
couplepremiumLabel = Label(paketFrame, text='Couple Premium', font=('times new roman', 15, 'bold'),
                           bg='gray20', fg='white')
couplepremiumLabel.grid(row=7, column=0, pady=7, padx=10)

# entrycouplepremium
couplepremiumEntry = Entry(paketFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
couplepremiumEntry.grid(row=7, column=1, pady=6, padx=10)
couplepremiumEntry.insert(0,0)


# labelgrouppremium
grouppremiumLabel = Label(paketFrame, text='Group Premium', font=('times new roman', 15, 'bold'),
                          bg='gray20', fg='white')
grouppremiumLabel.grid(row=8, column=0, pady=6, padx=10)

# entrygrouppremium
grouppremiumEntry = Entry(paketFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
grouppremiumEntry.grid(row=8, column=1, pady=6, padx=10)
grouppremiumEntry.insert(0,0)



#------------------------------------------------------------------------------------------------------#
#frame additional
additionalFrame = LabelFrame(productsFrame, text='Additional', font=('arial', 15, 'bold'),
                        fg='gold', bd=8, relief=GROOVE, bg='gray20')

additionalFrame.grid(row=0,column=1)

#addtimelabel
addtimeLabel=Label(additionalFrame,text='Add Time',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
addtimeLabel.grid(row=1,column=0,pady=41,padx=10)

#entryaddtime
addtimeEntry=Entry(additionalFrame, font=('times new roman',15,'bold'),width=10,bd=5)
addtimeEntry.grid(row=1,column=1,pady=41,padx=10)
addtimeEntry.insert(0,0)

#

#addprintfoto
addprintfotoLabel=Label(additionalFrame,text='Add Print Foto',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
addprintfotoLabel.grid(row=2,column=0,pady=41,padx=10)

#entryaddprintfoto
addprintfotoEntry=Entry(additionalFrame, font=('times new roman',15,'bold'),width=10,bd=5)
addprintfotoEntry.grid(row=2,column=1,pady=41,padx=10)
addprintfotoEntry.insert(0,0)

#

#labeladdperson
addpersonLabel=Label(additionalFrame,text='Add Person',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
addpersonLabel.grid(row=3,column=0,pady=41,padx=10)

#entryaddperson
addpersonEntry=Entry(additionalFrame, font=('times new roman',15,'bold'),width=10,bd=5)
addpersonEntry.grid(row=3,column=1,pady=41,padx=10)
addpersonEntry.insert(0,0)

#-------------------------------------------------------------------------------------------#

#frame aksesoris
aksesorisFrame = LabelFrame(productsFrame, text='Aksesoris', font=('arial', 15, 'bold'),
                        fg='gold', bd=8, relief=GROOVE, bg='gray20')

aksesorisFrame.grid(row=0,column=2)

#labelbando
aksesorisbandoLabel=Label(aksesorisFrame,text='Bando',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
aksesorisbandoLabel.grid(row=1,column=0,pady=2,padx=10)

#entrybando
aksesorisbandoEntry=Entry(aksesorisFrame, font=('times new roman',15,'bold'),width=10,bd=5)
aksesorisbandoEntry.grid(row=1,column=1,pady=2,padx=10)
aksesorisbandoEntry.insert(0,0)


#
#addbungapalsu
aksesorisbungapalsuLabel=Label(aksesorisFrame,text='Bunga Palsu',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
aksesorisbungapalsuLabel.grid(row=2,column=0,pady=2,padx=10)

#entrybungapalsu
aksesorisbungapalsuEntry=Entry(aksesorisFrame, font=('times new roman',15,'bold'),width=10,bd=5)
aksesorisbungapalsuEntry.grid(row=2,column=1,pady=2,padx=10)
aksesorisbungapalsuEntry.insert(0,0)

#
#addlatar
aksesorislatarLabel=Label(aksesorisFrame,text='Latar',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
aksesorislatarLabel.grid(row=3,column=0,pady=2,padx=10)

#entrylatar
aksesorislatarEntry=Entry(aksesorisFrame, font=('times new roman',15,'bold'),width=10,bd=5)
aksesorislatarEntry.grid(row=3,column=1,pady=2,padx=10)
aksesorislatarEntry.insert(0,0)

#
#addboneka
aksesorisbonekaLabel=Label(aksesorisFrame,text='Boneka',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
aksesorisbonekaLabel.grid(row=4,column=0,pady=2,padx=10)

#entryboneka
aksesorisbonekaEntry=Entry(aksesorisFrame, font=('times new roman',15,'bold'),width=10,bd=5)
aksesorisbonekaEntry.grid(row=4,column=1,pady=2,padx=10)
aksesorisbonekaEntry.insert(0,0)


#
#addkacamata
aksesoriskacamataLabel=Label(aksesorisFrame,text='Kacamata',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
aksesoriskacamataLabel.grid(row=5,column=0,pady=2,padx=10)

#entrykacamata
aksesoriskacamataEntry=Entry(aksesorisFrame, font=('times new roman',15,'bold'),width=10,bd=5)
aksesoriskacamataEntry.grid(row=5,column=1,pady=2,padx=10)
aksesoriskacamataEntry.insert(0,0)


#
#addpedang
aksesorispedangLabel=Label(aksesorisFrame,text='Pedang',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
aksesorispedangLabel.grid(row=6,column=0,pady=2,padx=10)

#entrypedang
aksesorispedangEntry=Entry(aksesorisFrame, font=('times new roman',15,'bold'),width=10,bd=5)
aksesorispedangEntry.grid(row=6,column=1,pady=2,padx=10)
aksesorispedangEntry.insert(0,0)

#
#addperisai
aksesorisperisaiLabel=Label(aksesorisFrame,text='Perisai',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
aksesorisperisaiLabel.grid(row=7,column=0,pady=2,padx=10)

#entryperisai
aksesorisperisaiEntry=Entry(aksesorisFrame, font=('times new roman',15,'bold'),width=10,bd=5)
aksesorisperisaiEntry.grid(row=7,column=1,pady=2,padx=10)
aksesorisperisaiEntry.insert(0,0)

#
#addpakaiankustom
aksesorispakaiankustomLabel=Label(aksesorisFrame,text='Pakaian Kustom',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
aksesorispakaiankustomLabel.grid(row=8,column=0,pady=2,padx=10)

#entrypakaiankustom
aksesorispakaiankustomEntry=Entry(aksesorisFrame, font=('times new roman',15,'bold'),width=10,bd=5)
aksesorispakaiankustomEntry.grid(row=8,column=1,pady=2,padx=10)
aksesorispakaiankustomEntry.insert(0,0)

#
#adddasi
aksesorisdasiLabel=Label(aksesorisFrame,text='Dasi',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
aksesorisdasiLabel.grid(row=9,column=0,pady=2,padx=10)

#entrydasi
aksesorisdasiEntry=Entry(aksesorisFrame, font=('times new roman',15,'bold'),width=10,bd=5)
aksesorisdasiEntry.grid(row=9,column=1,pady=2,padx=10)
aksesorisdasiEntry.insert(0,0)

#-------------------------------------------------------------------------------------------#

#frame struk
strukarea=LabelFrame(productsFrame, bd=8, relief=GROOVE)
strukarea.grid(row=0,column=3)

strukareaLabel=Label(strukarea,text='Struk Area',font=('times new roman',15,'bold'), bd=7, relief=GROOVE)
strukareaLabel.pack(fill=X)

scrollbar=Scrollbar(strukarea, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea=Text(strukarea,height=20,width=41,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

#-------------------------------------------------------------------------------------------#

#frame menu Pembayaran
menupembayaranFrame = LabelFrame(root, text='Rincian Pembayaran', font=('times new roman', 15, 'bold'),
                        fg='gold', bd=8, relief=GROOVE, bg='gray20')

menupembayaranFrame.pack()

#1
totalhargapaketLabel=Label(menupembayaranFrame,text='Paket',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
totalhargapaketLabel.grid(row=0,column=0,pady=2,padx=15)

#entrylatar
totalhargapaketEntry=Entry(menupembayaranFrame, font=('times new roman',15,'bold'),width=10,bd=5)
totalhargapaketEntry.grid(row=0,column=1,pady=9,padx=15,sticky='w')

#

#2
totalhargaadditionalLabel=Label(menupembayaranFrame,text='Additional',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
totalhargaadditionalLabel.grid(row=1,column=0,pady=2,padx=15)

#entrylatar
totalhargaadditionalEntry=Entry(menupembayaranFrame, font=('times new roman',15,'bold'),width=10,bd=5)
totalhargaadditionalEntry.grid(row=1,column=1,pady=9,padx=15,sticky='w')

#
#3
totalhargaaksesorisLabel=Label(menupembayaranFrame,text='Aksesoris',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
totalhargaaksesorisLabel.grid(row=2,column=0,pady=2,padx=15)

#entrylatar
totalhargaaksesorisEntry=Entry(menupembayaranFrame, font=('times new roman',15,'bold'),width=10,bd=5)
totalhargaaksesorisEntry.grid(row=2,column=1,pady=9,padx=15,sticky='w')

########################################

#1
totalpajakLabel=Label(menupembayaranFrame,text='Pajak',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
totalpajakLabel.grid(row=0,column=2,pady=2,padx=15)

#entrylatar
totalpajakEntry=Entry(menupembayaranFrame, font=('times new roman',15,'bold'),width=10,bd=5)
totalpajakEntry.grid(row=0,column=3,pady=9,padx=15,sticky='w')

#

#2
totaltransaksiLabel=Label(menupembayaranFrame,text='Total Transaksi',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
totaltransaksiLabel.grid(row=1,column=2,pady=2,padx=15)

#entrylatar
totaltransaksiEntry=Entry(menupembayaranFrame, font=('times new roman',15,'bold'),width=10,bd=5)
totaltransaksiEntry.grid(row=1,column=3,pady=9,padx=15,sticky='w')

##################

#1
totalbayarLabel=Label(menupembayaranFrame,text='Uang Bayar',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
totalbayarLabel.grid(row=0,column=4,pady=2,padx=15)

#entrylatar
totalbayarEntry=Entry(menupembayaranFrame, font=('times new roman',15,'bold'),width=10,bd=5)
totalbayarEntry.grid(row=0,column=5,pady=9,padx=15,sticky='w')

#2
totalkembalianLabel=Label(menupembayaranFrame,text='Kembalian',font=('times new roman',15,'bold'),
                    bg='gray20',fg='white')
totalkembalianLabel.grid(row=1,column=4,pady=2,padx=15)

#entrykembalian
totalkembalianEntry=Entry(menupembayaranFrame, font=('times new roman',15,'bold'),width=10,bd=5)
totalkembalianEntry.grid(row=1,column=5,pady=9,padx=15,sticky='w')

#------------------------------------------------------------------------------------------------------

buttonFrame=Frame(menupembayaranFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0,column=6,rowspan=3)

totalButton=Button(buttonFrame, text='Total', font=('arial',12,'bold'),bg='gray28',fg='white',
                   bd=5,width=8,padx=35,command=total)
totalButton.grid(row=0,column=0,pady=2,padx=15)

bayarButton = Button(buttonFrame, text='Bayar', font=('arial', 12, 'bold'), bg='gray28', fg='white',
                   bd=5, width=8, padx=35, command=bayar)
bayarButton.grid(row=0, column=1, pady=2, padx=15)


simpanButton=Button(buttonFrame, text='Simpan', font=('arial',12,'bold'),bg='gray28',fg='white',
                   bd=5,width=8,padx=34, command=simpan)
simpanButton.grid(row=1,column=0,pady=2,padx=15)

printButton=Button(buttonFrame, text='Print', font=('arial',12,'bold'),bg='gray28',fg='white',
                   bd=5,width=8,padx=34,command=print_struk)
printButton.grid(row=1,column=1,pady=2,padx=15)

resetButton=Button(buttonFrame, text='Reset', font=('arial',12,'bold'),bg='gray28',fg='white',
                   bd=5,width=8,padx=34,command=reset)
resetButton.grid(row=2,column=0,pady=2,padx=15)

keluarButton=Button(buttonFrame, text='Keluar', font=('arial',12,'bold'),bg='gray28',fg='white',
                   bd=5,width=8,padx=34,command=keluar)
keluarButton.grid(row=2,column=1,pady=2,padx=15)

#----------------------------------------------------------------------------------------------------------

root.mainloop()

