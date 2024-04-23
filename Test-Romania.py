# %%
from selenium import webdriver
from selenium.webdriver.common.by import By

# %%
wd = webdriver.Chrome()

# %%
url = "https://www.flashscore.ro/meci/d2sRDNXf/#/sumar-meci/echipele-de-start"

# %%
wd.get(url)

# %%
wd.find_element(By.ID, "onetrust-accept-btn-handler").click()

# %%
romania_full_xpath = '/html/body/div[1]/div/div[8]/div[2]/div/div[1]'

romania_xpath_originial = '//*[@id="detail"]/div[8]/div[2]/div/div[1]'

romania_xpath = '//div[@id="detail"]//div[@class="lf__field"]/div[1]'

romania_xpath = '//div[@id="detail"]//div[contains=(@class, "lf__formationDense")]'

romania_xpath = '//div[@id="detail"]//div[@class="lf__formation lf__formationDense"]'




# %%
len(wd.find_elements(By.XPATH, romania_xpath_originial))

# %%
jucatorii_romaniei_xpath = romania_xpath + '//span[@class="lf__playerNameText"]'
jucatorii_romaniei_xpath

# %%
jucatori = wd.find_elements(By.XPATH, jucatorii_romaniei_xpath)
len(wd.find_elements(By.XPATH, jucatorii_romaniei_xpath))

# %%


# %%
", ".join([j.text for j in jucatori])

# %%
titulari_xpath = "//div[@class='lf__sidesBox']"
titulari_romania = titulari_xpath + '/div[@class="lf__sides"]/div[1]'

nume_jucatori = titulari_romania + "//a[@class='lf__participantName']/div"



# %%
len(wd.find_elements(By.XPATH, nume_jucatori))
titulari = wd.find_elements(By.XPATH, nume_jucatori)
# for juc in titulari:
#     print(juc.text)

# %%
text = 'Titulari'
titulari_section_xpath = '//div[contains(text(), "Titulari")]'
titulari_div = wd.find_elements(By.XPATH, titulari_section_xpath)
titulari_div = titulari_div[0]


# %%

titulari_section = titulari_div.find_element(By.XPATH, '..')
titulari_section

# %%
len( titulari_section.find_elements(By.XPATH, 'div[@class="lf__sidesBox"]/div/div[1]//a[@class="lf__participantName"]/div'))

# %%
titulari_romania = titulari_section.find_elements(By.XPATH, 'div[@class="lf__sidesBox"]/div/div[1]//a[@class="lf__participantName"]/div')
len(titulari_romania)
", ".join([j.text for j in titulari_romania])

# %%
titulari_romania = titulari_section.find_elements(By.CSS_SELECTOR,"div.lf__side:nth-child(1) a.lf__participantName div" )
len(titulari_romania)
", ".join([j.text for j in titulari_romania])

# %%
xpath_field = '//div[@class="lf__field"]'
field = wd.find_element(By.XPATH, xpath_field)
field

# %%
galbene_xpath =  xpath_field + '//*[@class="card-ico yellowCard-ico"]'
galbene_xpath
len(wd.find_elements(By.XPATH, galbene_xpath))

# %%
lista_galbene = wd.find_elements(By.XPATH, galbene_xpath)

# %%
primul_galben = lista_galbene[0]
primul_galben.find_element(By.XPATH, "..").get_attribute("title")

# %%
for galben in lista_galbene:
    print(galben.find_element(By.XPATH, "..").get_attribute("title"))

# %%
sorted([galben.find_element(By.XPATH, "..").get_attribute("title") for galben in lista_galbene])

# %%
goluri_xpath =  xpath_field + '//*[@data-testid="wcl-icon-soccer"]'
goluri_xpath
len(wd.find_elements(By.XPATH, goluri_xpath))

# %%
goluri_svg_list = wd.find_elements(By.XPATH, goluri_xpath)
goluri_svg_list
for gol in goluri_svg_list:
    print(gol.find_element(By.XPATH, '..').get_attribute("title"))

# %%
goluri_svg_list = wd.find_elements(By.XPATH, goluri_xpath)
for gol in goluri_svg_list:
    print(gol.find_element(By.XPATH, '../../../a[@class="lf__playerName"]//span[@class="lf__playerNameText"]').text)


