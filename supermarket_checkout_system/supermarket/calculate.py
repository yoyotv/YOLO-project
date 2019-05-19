import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt
from time import gmtime, strftime


name_list=["adelholzener_alpenquelle_classic_075","adelholzener_alpenquelle_naturell_075","adelholzener_classic_bio_apfelschorle_02","adelholzener_classic_naturell_02","adelholzener_gourmet_mineralwasser_02","augustiner_lagerbraeu_hell_05","augustiner_weissbier_05","coca_cola_05","coca_cola_light_05","suntory_gokuri_lemonade","tegernseer_hell_03","corny_nussvoll","corny_nussvoll_single","corny_schoko_banane","corny_schoko_banane_single","dr_oetker_vitalis_knuspermuesli_klassisch","koelln_muesli_fruechte","koelln_muesli_schoko","caona_cocoa","cocoba_cocoa","cafe_wunderbar_espresso","douwe_egberts_professional_ground_coffee","gepa_bio_caffe_crema","gepa_italienischer_bio_espresso","apple_braeburn_bundle","apple_golden_delicious","apple_granny_smith","apple_red_boskoop,avocado","banana_bundle","banana_single","clementine,clementine_single","grapes_green_sugraone_seedless","grapes_sweet_celebration_seedless","kiwi,orange_single","oranges,pear","pasta_reggia_elicoidali","pasta_reggia_fusilli","pasta_reggia_spaghetti","franken_tafelreiniger","pelikan_tintenpatrone_canon","ethiquable_gruener_tee_ceylon","gepa_bio_und_fair_fencheltee","gepa_bio_und_fair_kamillentee","gepa_bio_und_fair_kraeuterteemischung","gepa_bio_und_fair_pfefferminztee","gepa_bio_und_fair_rooibostee","kilimanjaro_tea_earl_grey","cucumber","carrot","corn_salad","lettuce","vine_tomatoes","roma_vine_tomatoes,rocket","salad_iceberg","zucchini"]
price_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
#print name_list[0]
def find_price(product_name,name_list,price_list):
    for i in range(len(name_list)):
        if product_name == name_list[i]:
            return price_list[i]

#prediction = Image.open("/home/pi/darknet/predictions.jpg")
#prediction = np.asarray(prediction)
#h = prediction.shape[0]
#w = prediction.shape[1]
#prediction.setflags(write=1)
#prediction[int(h*0.75-h*0.28/2):int(h*0.75+h*0.28/2),int(w*0.22-w*0.15/2):int(w*0.22+w*0.15/2),:] = 0

with open("/home/pi/Desktop/supermarket/current_record/predictions.txt",'r') as file:
    ans = file.readlines()


total = 0
for i in range(len(ans)):
    #print ans[i][:-1]
    current = find_price(ans[i][:-1],name_list,price_list)
    total = total + current
    
print "Total price is " + str(total)    


file_name = "/home/pi/Desktop/supermarket/records/" + strftime("%Y_%m_%d_%H:%M:%S",gmtime()) + '.txt'
with open(file_name,'w') as file:
    for i in range(len(ans)):
        file.write(str(ans[i]))
    file.write("\n")
    file.write("Total price is " + str(total))