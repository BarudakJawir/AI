import numpy as np
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from sklearn.model_selection import train_test_split
import xlsxwriter

# Load data from Excel
data = pd.read_excel('data_outlet_mi_ayam.xlsx') 

# Input variables
kebersihan = ctrl.Antecedent(np.arange(1, 10, 1), 'kebersihan')
rasa = ctrl.Antecedent(np.arange(1, 10, 1), 'rasa')
harga = ctrl.Antecedent(np.arange(1, 10, 1), 'harga')

# Output variable
kelayakan = ctrl.Consequent(np.arange(1, 10, 1), 'kelayakan')

# Membership functions
kebersihan.automf(3)
rasa.automf(3)
harga.automf(3)
kelayakan.automf(3)

# Rules
rule1 = ctrl.Rule(kebersihan['poor'] | rasa['poor'] | harga['poor'], kelayakan['poor'])
rule2 = ctrl.Rule(kebersihan['average'] | rasa['average'] | harga['average'], kelayakan['average'])
rule3 = ctrl.Rule(kebersihan['good'] | rasa['good'] | harga['good'], kelayakan['good'])
rule4 = ctrl.Rule(kebersihan['poor'] | rasa['good'] | harga['good'], kelayakan['good'])
rule5 = ctrl.Rule(kebersihan['poor'] | rasa['average'] | harga['good'], kelayakan['average'])
rule6 = ctrl.Rule(kebersihan['poor'] | rasa['poor'] | harga['good'], kelayakan['average'])





# Control System
kelayakan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
kelayakan_sim = ctrl.ControlSystemSimulation(kelayakan_ctrl)

# Rentang nilai untuk kategori kelayakan
batas_kurang_layak = 3
batas_layak = 5.5

hasil_kelayakan = []
tingkatan_kelayakan = []

print('Kelayakan outlet mi ayam')
print('_________________________')


# Evaluasi untuk setiap outlet
for nomor_outlet in data['nomor_outlet']:
    # Dapatkan data untuk outlet saat ini
    data_outlet = data[data['nomor_outlet'] == nomor_outlet]
    kebersihan_val = data_outlet['kebersihan'].values[0]
    rasa_val = data_outlet['rasa'].values[0]
    harga_val = data_outlet['harga'].values[0]

    # Hitung tingkat kelayakan
    kelayakan_sim.input['kebersihan'] = kebersihan_val
    kelayakan_sim.input['rasa'] = rasa_val
    kelayakan_sim.input['harga'] = harga_val
    kelayakan_sim.compute()
    tingkat_kelayakan = round(kelayakan_sim.output['kelayakan'], 1)  # Bulatkan ke satu angka dibelakang koma

    # Tentukan kategori kelayakan
    if tingkat_kelayakan <= batas_kurang_layak:
        kategori_kelayakan = "Tidak Layak"
    elif tingkat_kelayakan <= batas_layak:
        kategori_kelayakan = "Kurang Layak"
    else:
        kategori_kelayakan = "Layak"

    # Cetak tingkat kelayakan untuk outlet saat ini
    print(f"No. Outlet {nomor_outlet}")
    print(f"Tingkat Kelayakan: {tingkat_kelayakan}")
    print(f"Kategori Kelayakan: {kategori_kelayakan}\n")

    hasil_kelayakan.append(tingkat_kelayakan)
    tingkatan_kelayakan.append(kategori_kelayakan)

data['Tingkat Kelayakan'] = hasil_kelayakan
data['Kategori Kelayakan'] = tingkatan_kelayakan
data.to_excel('hasil_kelayakan_outlet_mi_ayam.xlsx', index=False)  
