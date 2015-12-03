# update college data using the Dept. of Education's collegechoice api
import pprint
import time
import datetime
import sys

from paying_for_college.disclosures.scripts.api_utils import *
from paying_for_college.models import School, 

PP = pprint.PrettyPrinter(indent=4)
ID_BASE = "%s?api_key=%s" % (schools_root, api_key)
FAILED = []
NO_DATA = []
# school ids for which ED has no ope6 or ope8
# SKIP = [100636, 100733, 101471, 103529, 104531, 104984, 105127, 105136, 106607, 108056, 108199, 109891, 110051, 110501, 112312, 112376, 112783, 112817, 113227, 113607, 113953, 114062, 114372, 114831, 114895, 115287, 116040, 116660, 117681, 117900, 118134, 119678, 120023, 120166, 121008, 121071, 121178, 121877, 122250, 122320, 122737, 122782, 123855, 123925, 124557, 125019, 125037, 125222, 125301, 125480, 126100, 126410, 128300, 128328, 128425, 128586, 128762, 129640, 130624, 130882, 131566, 134875, 135434, 136011, 136075, 136251, 136738, 136747, 137892, 138594, 138983, 139533, 139773, 140076, 140085, 140304, 140322, 140401, 140483, 140669, 140997, 141307, 141963, 143075, 144500, 144616, 144759, 144777, 146384, 148016, 148724, 149019, 149240, 149587, 150640, 150978, 150996, 151005, 151014, 151023, 151032, 151041, 151050, 151069, 151078, 151087, 151096, 151157, 151193, 151209, 151236, 151245, 151485, 152220, 152424, 154651, 154819, 154943, 156675, 157234, 157395, 157748, 157854, 158219, 158769, 159258, 159267, 159638, 159948, 160533, 160685, 160968, 161059, 161280, 161882, 163842, 164146, 164155, 164207, 164243, 164571, 166489, 166665, 167543, 168519, 169567, 172556, 172574, 172583, 172972, 174932, 175999, 176734, 176938, 177153, 177162, 177807, 177922, 178022, 178129, 178439, 178563, 178785, 179283, 181136, 181543, 181747, 182519, 182883, 182917, 183327, 183345, 183600, 184135, 184269, 185651, 187222, 190035, 190734, 191384, 191393, 192244, 192457, 192475, 192536, 192998, 193317, 193380, 193788, 194204, 194453, 195049, 195429, 195571, 195669, 195827, 195924, 197036, 198631, 199175, 200697, 201140, 202064, 202189, 202268, 202541, 202611, 203049, 203076, 203164, 203818, 204547, 204741, 205692, 205717, 206419, 206428, 209445, 210809, 212805, 213057, 214315, 214661, 215965, 216348, 216986, 217545, 218089, 222497, 222628, 222682, 222691, 222761, 224253, 224402, 224712, 224907, 225751, 226329, 228671, 228714, 228732, 229090, 229407, 229638, 230092, 230223, 231156, 231642, 232593, 233499, 234526, 234687, 237154, 237507, 238315, 238421, 238935, 239965, 240435, 242060, 242671, 243160, 247083, 247737, 247922, 248943, 249247, 250832, 250920, 260381, 262165, 363457, 363563, 364317, 364566, 364885, 365107, 366702, 366757, 367176, 367264, 367413, 368160, 368799, 369020, 372523, 373119, 373447, 374291, 374990, 375559, 375771, 375799, 375948, 376039, 377421, 377634, 379463, 380410, 380447, 381796, 382054, 384184, 384193, 384360, 384379, 384388, 384397, 387235, 397641, 400637, 403399, 404480, 405003, 406060, 406264, 407744, 408057, 408437, 409209, 409245, 409333, 409379, 410034, 412650, 413185, 413918, 414850, 417150, 417211, 417390, 417567, 417901, 418162, 419022, 419217, 419439, 419536, 419572, 420352, 420802, 420972, 423412, 423476, 423670, 424424, 425393, 428037, 428295, 428338, 428426, 430102, 430500, 431248, 432144, 432199, 432214, 433217, 434326, 436289, 436377, 436526, 436562, 436784, 436854, 437325, 437343, 437361, 437565, 437583, 437723, 437927, 438036, 438638, 438665, 438887, 438966, 439154, 439163, 439330, 439604, 439695, 439756, 440138, 440165, 440235, 440244, 440305, 440378, 440396, 440536, 440545, 440572, 440581, 440590, 440624, 440721, 440846, 440970, 441159, 441238, 441399, 441584, 441681, 441733, 441797, 442000, 442310, 442365, 442392, 442499, 442505, 442684, 442824, 442833, 442851, 443128, 443304, 443368, 443456, 443465, 443517, 443553, 443605, 443711, 443906, 443988, 443997, 444015, 444033, 444060, 444176, 444459, 444477, 444626, 444750, 445009, 445337, 445355, 445407, 445416, 445452, 445489, 445531, 445629, 445832, 446154, 446297, 446312, 446321, 446358, 446419, 446428, 446507, 446613, 446701, 446710, 446783, 446978, 447397, 447485, 447829, 447838, 448080, 448099, 448266, 448336, 448363, 448381, 448549, 448558, 448637, 448655, 448691, 448789, 448877, 448965, 449278, 449418, 449515, 449551, 449694, 449755, 449825, 449889, 449913, 449940, 450012, 450386, 450438, 450508, 450517, 450553, 450562, 450775, 450997, 451024, 451088, 451112, 451200, 451246, 451325, 451389, 451431, 451486, 451608, 451680, 451778, 451893, 452133, 452203, 452212, 452230, 452258, 452522, 452540, 452692, 452771, 452780, 452841, 452957, 452984, 453297, 453349, 453507, 453516, 453792, 453923, 454032, 454209, 454218, 454263, 454281, 454290, 454403, 454412, 454421, 454430, 454449, 454564, 454634, 454713, 455309, 455318, 455363, 455372, 455451, 455503, 455530, 455789, 455822, 456171, 456384, 456870, 456889, 456898, 456904, 456913, 456995, 457013, 457068, 457095, 457217, 457235, 457262, 457305, 457660, 457712, 457882, 457907, 457970, 458089, 458238, 458511, 458520, 458672, 459860, 459879, 459888, 459897, 459903, 459912, 459921, 459976, 460172, 460330, 460385, 460491, 460507, 460604, 460622, 460686, 461050, 461069, 461087, 461166, 461184, 461209, 461467, 461519, 462080, 462099, 462105, 462114, 462123, 462132, 462141, 462150, 462169, 462178, 462187, 462196, 462202, 462211, 462220, 462257, 462293, 462406, 463621, 470269, 474872, 475088, 475167, 475185, 475228, 475237, 475246, 475422, 475723, 475787, 475811, 475857, 476072, 476647, 476656, 476665, 479619, 480055, 480064, 480116, 480338, 480435, 480444, 480499, 480505, 480684, 480709, 480718, 480745, 481076, 481535, 481997, 482936, 483018, 483036, 483090]


def get_ids():
    starter = datetime.datetime.now()
    school_count = 0
    ope6_count = 0
    ope8_count = 0
    id_url = "%s&id=%s&fields=ope8_id,ope6_id,school.name"
    # for school in School.objects.all():
    schools = School.objects.filter(ope6_id=None)
    print("found %s schools needing id updates" % schools.count())
    for school in schools:
        school_count += 1
        sys.stdout.write('.')
        sys.stdout.flush()
        if school_count % 500 == 0:
            print(school_count)
            time.sleep(5)
        url = id_url % (ID_BASE, school.school_id)
        try:
            resp = requests.get(url)
        except:
            FAILED.append(school)
            continue
        else:
            if resp.ok:
                time.sleep(1)
                # print(school)
                data = resp.json()
                if data['results']:
                    results = data['results'][0]
                    if results['ope8_id']:
                        school.ope8_id = results['ope8_id']
                        ope8_count += 1
                    if results['ope6_id']:
                        school.ope6_id = results['ope6_id']
                        ope6_count += 1
                    school.save()
                    # PP.pprint(results)
                else:
                    # print("no data for %s" % school)
                    NO_DATA.append(school)
            else:
                FAILED.append(school)
                if resp.status_code == 429:
                    print("API limit reached")
                    print(resp.content)
                    break
                else:
                    print("request for %s returned %s" % (school,
                                                          resp.status_code))
                    continue
                continue
    endmsg = "checked %s schools\n\
    updated %s ope6 ids and %s ope8 ids\n\
    found no data for %s\n\
    failed to update %s\n\
    get_ids took %s to run" % (school_count,
                               ope6_count,
                               ope8_count,
                               len(NO_DATA),
                               len(FAILED),
                               (datetime.datetime.now()-starter))
    print(endmsg)
    return (FAILED, NO_DATA)
