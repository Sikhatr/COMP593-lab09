from tkinter import *
from tkinter import ttk
from poke_api import  get_pokemon_info
from tkinter import messagebox


# Create the window
root = Tk()
root.title("Pokeman info Viewer")
root.resizable(False, False)

# Additional window configuration
# Add frame to window
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

frm_btm_left = ttk.LabelFrame(root, text='Info')
frm_btm_left.grid(row=1, column=0, padx=(10,0), pady=10, sticky=N )

frm_btm_right = ttk.LabelFrame(root, text='Stats')
frm_btm_right.grid(row=1, column=1, padx=10, pady=(0,10), sticky=N)

#Add widgets to top frameS
lbl_name = ttk.Label(frm_top, text='Pokeman Name:')
lbl_name.grid(row=0, column=0, padx=10, pady=10)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1, padx=10, pady=10)

def get_info_button_click():
    # Get the name of the Pokeman
    poke_name = ent_name.get().strip()
    if poke_name == '':
        return

    # Get the Pokemon info from the PokeAPI
    poke_info = get_pokemon_info(poke_name)
    if poke_info is None:
       err_msg = f"Unable to get information from the PokeAPI for {poke_name}."
       messagebox.showinfo(title='Error', message=err_msg, icon='error')
       return

    #Populate the info values
    lbl_Height_value['text'] = f"{poke_info[1]['Height']} dm"
    lbl_weight_value['text'] = f"{poke_info['Weight']} hg"
    
    #Populate the stat values
    prg_hp['value'] = poke_info['stats'][0]['base_stat']
    prg_attack['value'] = poke_info['stats'][1]['base_stat']
    prg_defense['value'] = poke_info['stats'][2]['base_stat']
    prg_spcl_attack['value'] = poke_info['stats'][3]['base_stat']
    prg_spcl_defense['value'] = poke_info['stats'][4]['base_stat']
    prg_speed['value'] = poke_info['stats'][5]['base_stat']
    return
    

btn_get_info = ttk.Button(frm_top, text='Get Info', command=get_info_button_click)
btn_get_info.grid(row=0, column=2, padx=10, pady=10)

#Add widgets to bottom left frame
lbl_Height = ttk.Label(frm_btm_left, text='Height:')
lbl_Height.grid(row=0, column=0, sticky=NE)

lbl_Height_value = ttk.Label(frm_btm_left, text='')
lbl_Height_value.grid(row=0, column=1)

lbl_weight = ttk.Label(frm_btm_left, text='Weight:')
lbl_weight.grid(row=1, column=0, sticky=E)

lbl_weight_value = ttk.Label(frm_btm_left, text='')
lbl_weight_value.grid(row=1, column=1)

#Add widgets to bottom right frame
lbl_hP= ttk.Label(frm_btm_right, text='HP:')
lbl_hP.grid(row=0, column=0, sticky=E)
prg_hp = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL,length=200, maximum=255)
prg_hp.grid(row=0, column=1, padx=(0,5))

lbl_attack= ttk.Label(frm_btm_right, text='Attack:')
lbl_attack.grid(row=1, column=0, sticky=E)
prg_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL,length=200, maximum=255)
prg_attack.grid(row=1, column=1, pady=5, padx=(0,5))

lbl_defense= ttk.Label(frm_btm_right, text='Defense:')
lbl_defense.grid(row=2, column=0, sticky=E)
prg_defense = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL,length=200, maximum=255)
prg_defense.grid(row=2, column=1, pady=5, padx=(0,5))

lbl_spcl_attack= ttk.Label(frm_btm_right, text='Special Attack:')
lbl_spcl_attack.grid(row=3, column=0, sticky=E)
prg_spcl_attack = ttk.Progressbar(frm_btm_right, orient=HORIZONTAL,length=200, maximum=255)
prg_spcl_attack.grid(row=3, column=1, padx=(0,5))


lbl_spcl_defense= ttk.Label(frm_btm_right, text='Special Defense:')
lbl_spcl_defense.grid(row=4, column=0, padx=10, pady=10, sticky=E)
prg_spcl_defense= ttk.Progressbar(frm_btm_right, orient=HORIZONTAL,length=200, maximum=255)
prg_spcl_defense.grid(row=4, column=1, padx=10, pady=10)

lbl_speed= ttk.Label(frm_btm_right, text='Speed:')
lbl_speed.grid(row=5, column=0, sticky=E)
prg_speed= ttk.Progressbar(frm_btm_right, orient=HORIZONTAL,length=200, maximum=255)
prg_speed.grid(row=5, column=1, padx=(0,5))

# Loop until window is closed
root.mainloop()