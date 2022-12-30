import mcschematic
from PIL import Image
import json

#color: rgba, block: minecraft ID of block
blocks = [
{'color':(168, 90, 50, 255),'block':'acacia_planks'},
{'color':(103, 96, 86, 255),'block':'acacia_wood'},
{'color':(136, 136, 136, 255),'block':'andesite'},
{'color':(192, 175, 121, 255),'block':'birch_planks'},
{'color':(216, 215, 210, 255),'block':'birch_wood'},
{'color':(42, 35, 40, 255),'block':'blackstone'},
{'color':(8, 10, 15, 255),'block':'black_concrete'},
{'color':(25, 26, 31, 255),'block':'black_concrete_powder'},
{'color':(67, 30, 32, 255),'block':'black_glazed_terracotta'},
{'color':(25, 25, 25, 117),'block':'black_stained_glass'},
{'color':(37, 22, 16, 255),'block':'black_terracotta'},
{'color':(20, 21, 25, 255),'block':'black_wool'},
{'color':(44, 46, 143, 255),'block':'blue_concrete'},
{'color':(70, 73, 166, 255),'block':'blue_concrete_powder'},
{'color':(47, 64, 139, 255),'block':'blue_glazed_terracotta'},
{'color':(116, 167, 253, 255),'block':'blue_ice'},
{'color':(51, 76, 178, 121),'block':'blue_stained_glass'},
{'color':(74, 59, 91, 255),'block':'blue_terracotta'},
{'color':(53, 57, 157, 255),'block':'blue_wool'},
{'color':(150, 97, 83, 255),'block':'bricks'},
{'color':(96, 59, 31, 255),'block':'brown_concrete'},
{'color':(125, 84, 53, 255),'block':'brown_concrete_powder'},
{'color':(119, 106, 85, 255),'block':'brown_glazed_terracotta'},
{'color':(149, 111, 81, 255),'block':'brown_mushroom_block'},
{'color':(102, 76, 51, 117),'block':'brown_stained_glass'},
{'color':(77, 51, 35, 255),'block':'brown_terracotta'},
{'color':(114, 71, 40, 255),'block':'brown_wool'},
{'color':(47, 23, 28, 255),'block':'chiseled_nether_bricks'},
{'color':(53, 48, 56, 255),'block':'chiseled_polished_blackstone'},
{'color':(231, 226, 218, 255),'block':'chiseled_quartz_block'},
{'color':(183, 96, 27, 255),'block':'chiseled_red_sandstone'},
{'color':(216, 202, 155, 255),'block':'chiseled_sandstone'},
{'color':(119, 118, 119, 255),'block':'chiseled_stone_bricks'},
{'color':(160, 166, 179, 255),'block':'clay'},
{'color':(16, 15, 15, 255),'block':'coal_block'},
{'color':(116, 116, 116, 255),'block':'coal_ore'},
{'color':(119, 85, 59, 255),'block':'coarse_dirt'},
{'color':(127, 127, 127, 255),'block':'cobblestone'},
{'color':(40, 20, 23, 255),'block':'cracked_nether_bricks'},
{'color':(43, 37, 43, 255),'block':'cracked_polished_blackstone_bricks'},
{'color':(118, 117, 118, 255),'block':'cracked_stone_bricks'},
{'color':(92, 25, 29, 255),'block':'crimson_hyphae'},
{'color':(101, 48, 70, 255),'block':'crimson_planks'},
{'color':(32, 10, 60, 255),'block':'crying_obsidian'},
{'color':(21, 119, 136, 255),'block':'cyan_concrete'},
{'color':(36, 147, 157, 255),'block':'cyan_concrete_powder'},
{'color':(52, 118, 125, 255),'block':'cyan_glazed_terracotta'},
{'color':(76, 127, 153, 117),'block':'cyan_stained_glass'},
{'color':(86, 91, 91, 255),'block':'cyan_terracotta'},
{'color':(21, 137, 145, 255),'block':'cyan_wool'},
{'color':(66, 43, 20, 255),'block':'dark_oak_planks'},
{'color':(60, 46, 26, 255),'block':'dark_oak_wood'},
{'color':(51, 91, 75, 255),'block':'dark_prismarine'},
{'color':(124, 117, 114, 255),'block':'dead_brain_coral_block'},
{'color':(131, 123, 119, 255),'block':'dead_bubble_coral_block'},
{'color':(131, 123, 119, 255),'block':'dead_fire_coral_block'},
{'color':(133, 126, 122, 255),'block':'dead_horn_coral_block'},
{'color':(130, 123, 119, 255),'block':'dead_tube_coral_block'},
{'color':(98, 237, 228, 255),'block':'diamond_block'},
{'color':(125, 142, 141, 255),'block':'diamond_ore'},
{'color':(188, 188, 188, 255),'block':'diorite'},
{'color':(134, 96, 67, 255),'block':'dirt'},
{'color':(42, 203, 87, 255),'block':'emerald_block'},
{'color':(117, 136, 124, 255),'block':'emerald_ore'},
{'color':(219, 222, 158, 255),'block':'end_stone'},
{'color':(218, 224, 162, 255),'block':'end_stone_bricks'},
{'color':(140, 149, 151, 64),'block':'glass'},
{'color':(246, 208, 61, 255),'block':'gold_block'},
{'color':(143, 140, 125, 255),'block':'gold_ore'},
{'color':(149, 103, 85, 255),'block':'granite'},
{'color':(131, 127, 126, 255),'block':'gravel'},
{'color':(54, 57, 61, 255),'block':'gray_concrete'},
{'color':(76, 81, 84, 255),'block':'gray_concrete_powder'},
{'color':(83, 90, 93, 255),'block':'gray_glazed_terracotta'},
{'color':(76, 76, 76, 117),'block':'gray_stained_glass'},
{'color':(57, 42, 35, 255),'block':'gray_terracotta'},
{'color':(62, 68, 71, 255),'block':'gray_wool'},
{'color':(73, 91, 36, 255),'block':'green_concrete'},
{'color':(97, 119, 44, 255),'block':'green_concrete_powder'},
{'color':(117, 142, 67, 255),'block':'green_glazed_terracotta'},
{'color':(102, 127, 51, 117),'block':'green_stained_glass'},
{'color':(76, 83, 42, 255),'block':'green_terracotta'},
{'color':(84, 109, 27, 255),'block':'green_wool'},
{'color':(229, 148, 29, 255),'block':'honeycomb_block'},
{'color':(145, 183, 253, 190),'block':'ice'},
{'color':(220, 220, 220, 255),'block':'iron_block'},
{'color':(136, 130, 127, 255),'block':'iron_ore'},
{'color':(160, 115, 80, 255),'block':'jungle_planks'},
{'color':(85, 67, 25, 255),'block':'jungle_wood'},
{'color':(30, 67, 140, 255),'block':'lapis_block'},
{'color':(99, 110, 132, 255),'block':'lapis_ore'},
{'color':(35, 137, 198, 255),'block':'light_blue_concrete'},
{'color':(74, 180, 213, 255),'block':'light_blue_concrete_powder'},
{'color':(94, 164, 208, 255),'block':'light_blue_glazed_terracotta'},
{'color':(102, 153, 216, 117),'block':'light_blue_stained_glass'},
{'color':(113, 108, 137, 255),'block':'light_blue_terracotta'},
{'color':(58, 175, 217, 255),'block':'light_blue_wool'},
{'color':(125, 125, 115, 255),'block':'light_gray_concrete'},
{'color':(154, 154, 148, 255),'block':'light_gray_concrete_powder'},
{'color':(144, 166, 167, 255),'block':'light_gray_glazed_terracotta'},
{'color':(153, 153, 153, 117),'block':'light_gray_stained_glass'},
{'color':(135, 106, 97, 255),'block':'light_gray_terracotta'},
{'color':(142, 142, 134, 255),'block':'light_gray_wool'},
{'color':(94, 168, 24, 255),'block':'lime_concrete'},
{'color':(125, 189, 41, 255),'block':'lime_concrete_powder'},
{'color':(162, 197, 55, 255),'block':'lime_glazed_terracotta'},
{'color':(127, 204, 25, 117),'block':'lime_stained_glass'},
{'color':(103, 117, 52, 255),'block':'lime_terracotta'},
{'color':(112, 185, 25, 255),'block':'lime_wool'},
{'color':(169, 48, 159, 255),'block':'magenta_concrete'},
{'color':(192, 83, 184, 255),'block':'magenta_concrete_powder'},
{'color':(208, 100, 191, 255),'block':'magenta_glazed_terracotta'},
{'color':(178, 76, 216, 117),'block':'magenta_stained_glass'},
{'color':(149, 88, 108, 255),'block':'magenta_terracotta'},
{'color':(189, 68, 179, 255),'block':'magenta_wool'},
{'color':(114, 146, 30, 255),'block':'melon'},
{'color':(110, 118, 94, 255),'block':'mossy_cobblestone'},
{'color':(115, 121, 105, 255),'block':'mossy_stone_bricks'},
{'color':(66, 61, 63, 255),'block':'netherite_block'},
{'color':(97, 38, 38, 255),'block':'netherrack'},
{'color':(44, 21, 26, 255),'block':'nether_bricks'},
{'color':(115, 54, 42, 255),'block':'nether_gold_ore'},
{'color':(117, 65, 62, 255),'block':'nether_quartz_ore'},
{'color':(114, 2, 2, 255),'block':'nether_wart_block'},
{'color':(88, 58, 40, 255),'block':'note_block'},
{'color':(162, 130, 78, 255),'block':'oak_planks'},
{'color':(109, 85, 50, 255),'block':'oak_wood'},
{'color':(15, 10, 24, 255),'block':'obsidian'},
{'color':(224, 97, 0, 255),'block':'orange_concrete'},
{'color':(227, 131, 31, 255),'block':'orange_concrete_powder'},
{'color':(154, 147, 91, 255),'block':'orange_glazed_terracotta'},
{'color':(216, 127, 51, 117),'block':'orange_stained_glass'},
{'color':(161, 83, 37, 255),'block':'orange_terracotta'},
{'color':(240, 118, 19, 255),'block':'orange_wool'},
{'color':(141, 180, 250, 255),'block':'packed_ice'},
{'color':(213, 101, 142, 255),'block':'pink_concrete'},
{'color':(228, 153, 181, 255),'block':'pink_concrete_powder'},
{'color':(235, 154, 181, 255),'block':'pink_glazed_terracotta'},
{'color':(242, 127, 165, 117),'block':'pink_stained_glass'},
{'color':(161, 78, 78, 255),'block':'pink_terracotta'},
{'color':(237, 141, 172, 255),'block':'pink_wool'},
{'color':(132, 134, 133, 255),'block':'polished_andesite'},
{'color':(53, 48, 56, 255),'block':'polished_blackstone'},
{'color':(46, 41, 48, 255),'block':'polished_blackstone_bricks'},
{'color':(192, 193, 194, 255),'block':'polished_diorite'},
{'color':(154, 106, 89, 255),'block':'polished_granite'},
{'color':(99, 171, 158, 255),'block':'prismarine_bricks'},
{'color':(195, 114, 24, 255),'block':'pumpkin_side'},
{'color':(100, 31, 156, 255),'block':'purple_concrete'},
{'color':(131, 55, 177, 255),'block':'purple_concrete_powder'},
{'color':(109, 48, 152, 255),'block':'purple_glazed_terracotta'},
{'color':(127, 63, 178, 117),'block':'purple_stained_glass'},
{'color':(118, 70, 86, 255),'block':'purple_terracotta'},
{'color':(121, 42, 172, 255),'block':'purple_wool'},
{'color':(169, 125, 169, 255),'block':'purpur_block'},
{'color':(171, 128, 171, 255),'block':'purpur_pillar'},
{'color':(236, 230, 223, 255),'block':'quartz_block'},
{'color':(234, 229, 221, 255),'block':'quartz_bricks'},
{'color':(235, 229, 222, 255),'block':'quartz_pillar'},
{'color':(175, 24, 5, 255),'block':'redstone_block'},
{'color':(95, 54, 30, 255),'block':'redstone_lamp'},
{'color':(133, 107, 107, 255),'block':'redstone_ore'},
{'color':(142, 32, 32, 255),'block':'red_concrete'},
{'color':(168, 54, 50, 255),'block':'red_concrete_powder'},
{'color':(181, 59, 53, 255),'block':'red_glazed_terracotta'},
{'color':(200, 46, 45, 255),'block':'red_mushroom_block'},
{'color':(69, 7, 9, 255),'block':'red_nether_bricks'},
{'color':(190, 102, 33, 255),'block':'red_sand'},
{'color':(153, 51, 51, 151),'block':'red_stained_glass'},
{'color':(143, 61, 46, 255),'block':'red_terracotta'},
{'color':(160, 39, 34, 255),'block':'red_wool'},
{'color':(219, 207, 163, 255),'block':'sand'},
{'color':(158, 158, 158, 255),'block':'smooth_stone'},
{'color':(249, 254, 254, 255),'block':'snow_block'},
{'color':(81, 62, 50, 255),'block':'soul_sand'},
{'color':(75, 57, 46, 255),'block':'soul_soil'},
{'color':(195, 192, 74, 255),'block':'sponge'},
{'color':(58, 37, 16, 255),'block':'spruce_wood'},
{'color':(114, 84, 48, 255),'block':'spruce_planks'},
{'color':(125, 125, 125, 255),'block':'stone'},
{'color':(122, 121, 122, 255),'block':'stone_bricks'},
{'color':(174, 92, 59, 255),'block':'stripped_acacia_wood'},
{'color':(196, 176, 118, 255),'block':'stripped_birch_wood'},
{'color':(137, 57, 90, 255),'block':'stripped_crimson_hyphae'},
{'color':(96, 76, 49, 255),'block':'stripped_dark_oak_wood'},
{'color':(171, 132, 84, 255),'block':'stripped_jungle_wood'},
{'color':(177, 144, 86, 255),'block':'stripped_oak_wood'},
{'color':(115, 89, 52, 255),'block':'stripped_spruce_wood'},
{'color':(57, 150, 147, 255),'block':'stripped_warped_hyphae'},
{'color':(229, 176, 168, 255),'block':'target'},
{'color':(152, 94, 67, 255),'block':'terracotta'},
{'color':(58, 58, 77, 255),'block':'warped_hyphae'},
{'color':(43, 104, 99, 255),'block':'warped_planks'},
{'color':(22, 119, 121, 255),'block':'warped_wart_block'},
{'color':(171, 181, 70, 255),'block':'wet_sponge'},
{'color':(207, 213, 214, 255),'block':'white_concrete'},
{'color':(225, 227, 227, 255),'block':'white_concrete_powder'},
{'color':(188, 212, 202, 255),'block':'white_glazed_terracotta'},
{'color':(255, 255, 255, 117),'block':'white_stained_glass'},
{'color':(209, 178, 161, 255),'block':'white_terracotta'},
{'color':(233, 236, 236, 255),'block':'white_wool'},
{'color':(240, 175, 21, 255),'block':'yellow_concrete'},
{'color':(232, 199, 54, 255),'block':'yellow_concrete_powder'},
{'color':(234, 192, 88, 255),'block':'yellow_glazed_terracotta'},
{'color':(229, 229, 51, 117),'block':'yellow_stained_glass'},
{'color':(186, 133, 35, 255),'block':'yellow_terracotta'},
{'color':(248, 197, 39, 255),'block':'yellow_wool'},
]

blocktypes = {
    "falling_blocks" : [
        'gravel',
        'black_concrete_powder',
        'brown_concrete_powder',
        'cyan_concrete_powder',
        'blue_concrete_powder',
        'gray_concrete_powder',
        'green_concrete_powder',
        'light_blue_concrete_powder',
        'light_gray_concrete_powder',
        'lime_concrete_powder',
        'magenta_concrete_powder',
        'orange_concrete_powder',
        'pink_concrete_powder',
        'purple_concrete_powder',
        'red_sand',
        'red_concrete_powder',
        'sand',
        'white_concrete_powder',
        'yellow_concrete_powder']
}

def removeblocksbysettings(blocks_enabled):
    for i in blocks_enabled: 
        for key, val in i.items():
            if val == 1: break # if the blocks don't need to be removed, break 
            
            for i in range(len(blocks)): # for all blocks
                try:
                    if blocks[i]['block'] in blocktypes[key]: del blocks[i] # if block is in deleted list, delete
                except: break

def colordiff(pixelcolor, blockcolor):
    out = 0
    # add diffs together, and return
    for i in range(4):
        out += abs(pixelcolor[i] - blockcolor[i])
    return out

def findblockfromcolor(pixcolor):
    data = []
    # for all blocks, find color difference between image color and block
    for i in blocks:
        data.append({"colordiff":colordiff(pixcolor["color"],i["color"]),"block":i["block"]})

# find the pair with lowest color difference
    while len(data) > 1:
        if data[0]["colordiff"] < data[1]["colordiff"]: data.pop(1)
        else:                                           data.pop(0)
    data = data[0]
    # return the block with the lowest color difference to the skin
    return data["block"]

def combinedata(im, map):
    # get data from both images, and put into json. Also ready a "block" value
    image_val = list(im.getdata())
    map_val = list(map.getdata())
    conversions = []
    # combine into json
    for i in range(len(map_val)):
        conversions.append({
            "color":image_val[i],
            "pos":map_val[i],
            "block":""
            })

    # remove empty pixels
    out = []
    # if empty, delete
    for i in conversions:
        if i["color"][3] == 0 or i["pos"][3] == 0:
            continue
        else:
            out.append(i)
    return out

def main(im, map):
    schem = mcschematic.MCSchematic() # initialize schematic file
    conversions = combinedata(im, map) # convert image val into json
    removeblocksbysettings(settings["blocks_enabled"]) # remove disabled blocks from block list
    for i in range(len(conversions)):
        conversions[i]["block"] = findblockfromcolor(conversions[i]) # find block for specific color
    
    for i in conversions:
        x, y, z, *rest = i["pos"] # removes alpha value
        schem.setBlock((x, y, z), i["block"]) # places block into schematic from "conversions" value
    return schem

try:    mapping = Image.open(r'.\mapping_4px.png', 'r').convert("RGBA") # the RGB of the mapping file is used as XYZ, such that R=X, G=Y, B=Z
except: print('Could not locate mapping file. Please make sure you are CDd into this folder, and that the mapping file is there'); exit()
try:    skin = Image.open(r'.\skininput.png', 'r').convert("RGBA")
except: print('Missing input file. Please add your skin to this folder, and name it "skininput.png" '); exit()
with open("settings.json") as f:
    settings = json.load(f)

out = main(skin, mapping)
if settings["save_location"] == "": settings["save_location"] = './'
out.save(settings["save_location"], "skin2sta2_output", mcschematic.Version[settings["version"]])
print(f'Skin saved as schematic with version {settings["version"]} to {settings["save_location"]}')