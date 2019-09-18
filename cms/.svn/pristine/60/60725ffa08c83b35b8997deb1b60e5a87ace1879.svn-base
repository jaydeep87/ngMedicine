import requests
from elasticsearch import Elasticsearch
import master_list
from news.models import NewsFeed
from django.http import HttpResponse
# All index global list
# index_name = ["college", "degree", "registration_board", "zone", "zone_location", "designation", "days",


# Base URL
#base_url = "http://manojhfu:adminmanoj@es.healthforu.com/"
#base_url = "http://localhost:9200/"
base_url =  "http://103.53.197.173:9200/"
#es = Elasticsearch(['http://manojhfu:adminmanoj@es.healthforu.com:80'])
#es = Elasticsearch(['http://localhost:9200'])
es = Elasticsearch(['http://103.53.197.173:9200/'])
mapping_global_master = {
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "type": {
            "type": "string"
        }
    }
}

mapping_doctor = {
    "properties": {
        "attach_hospital_clinic": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "geo_point"
                },
                "consultancy_fees": {
                    "type": "integer"
                },
                "timing": {
                    "type": "object",
                    "properties": {
                        "start_time": {
                            "type": "date",
                            "format": "HH:mm:ss"
                        },
                        "end_time": {
                            "type": "date",
                            "format": "HH:mm:ss"  # review and dicuss
                        }
                    }

                },
                "timing": {
                    "type": "object",
                    "properties": {
                        "start_time": {
                            "type": "date",
                            "format": "HH:mm:ss"
                        },
                        "end_time": {
                            "type": "date",
                            "format": "HH:mm:ss"  # review and dicuss
                        }
                    }

                },

            }
        },
        "speciality": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            }
        },
        "service_offered": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            }
        },
        "mci": {
            "type": "string",
        },
        # "membership":{
        #     "type":"object"
        # },
        # "reward":{
        #     "type":"object"
        # },
        # "education":{
        #     "type":"object"
        # },
        #  "experience":{
        #     "type":"object"
        # },

    }
}

mapping_organisation = {
    "properties": {
        "name": {
            "type": "string"
        },
        "id": {
            "type": "integer"
        },
        "is_hospital": {
            "type": "boolean"
        },
        "is_clinic": {
            "type": "boolean"
        },
        "street": {
            "type": "string"
        },
        "locality_id": {
            "type": "integer"
        },
        "locality_name": {
            "type": "string"
        },
        "city_id": {
            "type": "integer"
        },
        "city_name": {
            "type": "string"
        },
        "state_id": {
            "type": "integer"
        },
        "state_name": {
            "type": "string"
        },
        "country_id": {
            "type": "integer"
        },
        "country_name": {
            "type": "string"
        },
        "phone": {
            "type": "string"
        },
        "mobile_no": {
            "type": "string"
        },
        "ambulance_service_no": {
            "type": "string"
        },
        "facility_list": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            }
        },
        "department_list": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            }
        },
        "niche_department": {
            "type": "string"
        },
        "brochure": {
            "type": "string"
        },
        "fax": {
            "type": "string"
        },
        "email": {
            "type": "string"
        },
        "emergency_no": {
            "type": "string"
        },
        "website": {
            "type": "string"
        },
        "category_list": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            }
        },
        "doctors_on_board": {
            "type": "string"
        },
        "type_list": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            }
        },
        "ambulance_service": {
            "type": "boolean"
        },
        "trauma_center": {
            "type": "boolean"
        },
        "burn_center": {
            "type": "boolean"
        },
        "establishmentYear": {
            "type": "string"
        },
        "geolocation": {
            "type": "geo_point"
        },
        "department_wise_doctor_list": {
            "type": "object"
        },
        "timing": {
            "type": "object",
            "properties": {
                "start_time": {
                    "type": "date",
                    "format": "HH:mm:ss"
                },
                "end_time": {
                    "type": "date",
                    "format": "HH:mm:ss"  # review and dicuss
                }
            }

        },
    }
}









#DJANGO MODEL = class Labs(models.Model):

mapping_lab = {
    "properties": {
        "id": {
            "type": "integer"
        },
        "address": {
            "type": "string"
        },
        "authorization_body": {
            "type": "string"
        },
        "locality_name": {
            "type": "string"
        },
        "locality_id": {
            "type": "integer"
        },
        "city_name": {
            "type": "string"
        },
        "city_id": {
            "type": "integer"
        },
        "state_name": {
            "type": "string"
        },
        "state_id": {
            "type": "integer"
        },
        "country_name": {
            "type": "string"
        },
        "country_id": {
            "type": "integer"
        },
        "home_sample_collection": {
            "type": "boolean"
        },
        "is_emergency": {
            "type": "boolean"
        },
        "lab_accreditation_body": {
            "type": "string"
        },
        "lab_authorised_person_contact_no": {
            "type": "string"
        },
        "lab_authorised_person_designation": {
            "type": "string"
        },
        "lab_authorised_person_emailid": {
            "type": "string"
        },
        "lab_authorised_person_name": {
            "type": "string"
        },
        "lab_collection_timing": {
            "type": "string"
        },
        "lab_departments": {
            "type": "string"
        },
        "lab_doctors_on_board": {
            "type": "string"
        },
        "lab_emailid": {
            "type": "string"
        },
        "lab_locality_coverage_from_id": {
            "type": "string"
        },
        "lab_locality_coverage_to_id": {
            "type": "string"
        },
        "lab_mobile": {
            "type": "string"
        },
        "lab_schedule": {
            "type": "object"
        },
        "lab_services": {
            "type": "string"
        },
        "lab_type_id": {
            "type": "integer"
        },
        "lab_website": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "pathology_doctor_name": {
            "type": "string"
        },
        "pathology_email": {
            "type": "string"
        },
        "pincode": {
            "type": "string"
        },
        "previous_user": {
            "type": "integer"
        },
        "rate": {
            "type": "float"
        },
        "ratings": {
            "type": "float"
        },
        "telephone": {
            "type": "string"
        },
        "tests": {
            "type": "string"
        },
        "timing": {
            "type": "object",
            "properties": {
                "start_time": {
                    "type": "date",
                    "format": "HH:mm:ss"
                },
                "end_time": {
                    "type": "date",
                    "format": "HH:mm:ss"  # review and dicuss
                }
            }

        },
    }
}

mapping_pharmacy = {
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "address": {
            "type": "string"
        },
        "locality_name": {
            "type": "string"
        },
        "locality_id": {
            "type": "integer"
        },
        "city_name": {
            "type": "string"
        },
        "city_id": {
            "type": "integer"
        },
        "state_name": {
            "type": "string"
        },
        "state_id": {
            "type": "integer"
        },
        "country_name": {
            "type": "string"
        },
        "country_id": {
            "type": "integer"
        },
        "pincode": {
            "type": "string"
        },
        "telephone": {
            "type": "string"
        },
        "mobile": {
            "type": "string"
        },
        "services": {
            "type": "string"
        },
        "contact_person": {
            "type": "string"
        },
        "type": {
            "type": "string"
        },
        "timings": {
            "type": "string"
        },
        "pharmacy_schedule": {
            "type": "object"
        },
        "is_emergency": {
            "type": "boolean"
        },
        "fax": {
            "type": "string"
        },
        "email": {
            "type": "string"
        },
        "website": {
            "type": "string"
        }
    }
}

mapping_healthtray = {
    "properties": {
        "id": {
            "type": "integer"
        },
        "health_tray_id": {
            "type": "integer"
        },
        "health_tray_name": {
            "type": "string"
        },
        "hfues_plan": {
            "type": "boolean"
        },
        "working_hours": {
            "type": "string"
        },
        "price_of_plan_after_discount": {
            "type": "string"
        },
        "plan_category_id": {
            "type": "integer"
        },
        "discount_on_plan": {
            "type": "string"
        },
        "age_group": {
            "type": "string"
        },
        "corporate_plan": {
            "type": "boolean"
        },
        "wellness_plan": {
            "type": "boolean"
        },
        "type": {
            "type": "string"
        },
        "user_category": {
            "type": "string"
        },
        "plan_price": {
            "type": "float"
        },
        "investigation": {
            "type": "object"
        },
        "consultation": {
            "type": "object"
        },
        "package_description": {
            "type": "string"
        },
        "plan_name": {
            "type": "string"
        },
        "is_life_service": {
            "type": "boolean"
        },
        "service_offered_in_plan": {
            "type": "string"
        },
        "is_home_service": {
            "type": "boolean"
        },
        "imaging": {
            "type": "object"
        },
        "others": {
            "type": "object"
        },
        "instructions": {
            "type": "string"
        },
        "nurse_plan": {
            "type": "boolean"
        },
        "plan_title": {
            "type": "string"
        },
        "is_enterprise_service": {
            "type": "boolean"
        },
        "timings": {
            "type": "string"
        },
        "plan_validity": {
            "type": "string"
        },
        "image_url": {
            "type": "string"
        },
        "no_of_employee": {
            "type": "string"
        }
    }
}

mapping_newsfeed = {
    "properties": {
        "id": {
            "type": "integer"
        },
        "doctors_category": {
            "type": "string"
        },
        "topic_title": {
            "type": "string"
        },
        "tag_string": {
            "type": "string"
        },
        "small_description": {
            "type": "string"
        },
        "newsfeed_html_refined": {
            "type": "string"
        },
        "newsfeed_image_file_name": {
            "type": "string"
        },
        "publish_date": {
            "type": "date"
        },
        "related_topics": {
            "type": "string"
        },
        "news_type_id": {
            "type": "integer"
        },
        "news_type_name": {
            "type": "string"
        }
    }
}

mapping_bloodbank = {
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "license": {
            "type": "string"
        },
        "address_1": {
            "type": "string"
        },
        "address_2": {
            "type": "string"
        },
        "locality_name": {
            "type": "string"
        },
        "locality_id": {
            "type": "integer"
        },
        "city_name": {
            "type": "string"
        },
        "city_id": {
            "type": "integer"
        },
        "state_name": {
            "type": "string"
        },
        "state_id": {
            "type": "integer"
        },
        "country_name": {
            "type": "string"
        },
        "country_id": {
            "type": "integer"
        },
        "pincode": {
            "type": "string"
        },
        "telephone": {
            "type": "string"
        },
        "mobile": {
            "type": "string"
        },
        "services": {
            "type": "string"
        },
        "blood_bank_doctor": {
            "type": "string"
        },
        "education": {
            "type": "string"
        },
        "stars": {
            "type": "float"
        },
        "timings": {
            "type": "string"
        },
        "bloodbank_schedule": {
            "type": "object"
        },
        "is_emergency": {
            "type": "boolean"
        },
        "pricing": {
            "type": "string"
        }
    }
}

mapping_ambulance = {
    "properties": {
        "id": {
            "type": "integer"
        },
        "ambulance_locality_coverage_to_id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "service": {
            "type": "string"
        },
        "locality_name": {
            "type": "string"
        },
        "locality_id": {
            "type": "integer"
        },
        "city_name": {
            "type": "string"
        },
        "city_id": {
            "type": "integer"
        },
        "state_name": {
            "type": "string"
        },
        "state_id": {
            "type": "integer"
        },
        "country_name": {
            "type": "string"
        },
        "country_id": {
            "type": "integer"
        },
        "pincode": {
            "type": "string"
        },
        "telephone": {
            "type": "string"
        },
        "mobile": {
            "type": "string"
        },
        "rates": {
            "type": "integer"
        },
        "service_contact_person": {
            "type": "string"
        },
        "address": {
            "type": "string"
        },
        "is_emergency": {
            "type": "string"
        },
        "type": {
            "type": "string"
        },
        "ambulance_locality_coverage_from_id": {
            "type": "integer"
        }
    }
}


# DJANGO MODEL  =      class Lab_branches(models.Model):
mapping_lab_branches = {
    "mappings": {
        "lab_branches_detail": {
            "properties": {
                "id": {
                    "type": "integer"
                },
                "lab_id": {
                    "type": "integer"
                },
                "lab_name": {
                    "type": "string"
                },
                "branches": {
                    "type": "?????????????? "
                },
            }
        }
    }
}



# DJANGO MODEL  =   class Labs_plan(models.Model):
mapping_lab_plans = {
    "mappings": {
        "lab_plans_detail": {
            "properties": {
                "id": {
                    "type": "integer"
                },
                "lab_id": {
                    "type": "integer"
                },
                "lab_name": {
                    "type": "string"
                },
                "package_details": {
                    "type": "?????????????? "
                },
            }
        }
    }
}


mapping_Lab_accreditation_body_master = {
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "sting"
        },
        "address": {
            "type": "sting"
        },
        "pincode": {
            "type": "sting"
        },
        "telephone": {
            "type": "sting"
        }
    }
}

mapping_symptom = {
    "properties": {
        "id": {
            "type": "integer"
        },
        "symptoms_html_refined": {
            "type": "string"
        },
        "doctors_category": {
            "type": "string"
        },
        "topic_title": {
            "type": "string"
        },
        "tag_string": {
            "type": "string"
        },
        "related_topics": {
            "type": "string"
        },
        "symptoms_image_file_name": {
            "type": "string"
        }
    }
}
mapping_disease = {
    "properties": {
        "id": {
            "type": "integer"
        },
        "disease_image_file_name": {
            "type": "string"
        },
        "doctors_category": {
            "type": "string"
        },
        "topic_title": {
            "type": "string"
        },
        "tag_string": {
            "type": "string"
        },
        "related_topics": {
            "type": "string"
        },
        "disease_html_refined": {
            "type": "string"
        }
    }
}


mapping_mater_organisation_branches = {
    "properties": {
        "id": {
            "type": "integer"
        },
        "branch_details": {
            "type": "object"
        }
    }
}

mapping_mater_lab_branches = {
    "properties": {
        "id": {
            "type": "integer"
        },
        "branch_details": {
            "type": "object"
        }
    }
}

mapping_rehabitation = {
    "properties": {
        "address": {
            "type": "string"
        },
        "city_id": {
            "type": "integer"
        },
        "city_name": {
            "type": "string"
        },
        "clinic_name": {
            "type": "string"
        },
        "country_id": {
            "type": "integer"
        },
        "country_name": {
            "type": "string"
        },
        "doctor_name": {
            "type": "string"
        },
        "id": {
            "type": "integer"
        },
        "is_emergency": {
            "type": "boolean"
        },
        "locality_id": {
            "type": "integer"
        },
        "locality_name": {
            "type": "string"
        },
        "mobile": {
            "type": "string"
        },
        "pincode": {
            "type": "string"
        },
        "speciality": {
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            }
        },
        "state_id": {
            "type": "integer"
        },
        "state_name": {
            "type": "string"
        },
        "telephone": {
            "type": "string"
        }
    }
}
####################################################################
# Name - mapping_define                                                #
# Owner - jitendra dixit
# testing:                                             #
# Review by -                                                 #
#                                                                  #
####################################################################


def mapping_define():
    doctor = "doctor"
    organisation = "organisation"
    lab = "lab"
    pharmacy = "pharmacy"
    bloodbank = "bloodbank"
    mapping_ambulance = "ambulance"

    newsfeed = "newsfeed"
    symptom = "symptom"
    disease = "disease"
    rehabitation = "rehabitation"
    labaccreditationmaster = "labaccreditation"
    try:
        # Three main Indices

        #HOME
        response = requests.put(base_url + str('home'))
        print(response.text)
        #newsfeed
        response = requests.put(base_url + str('home/_mapping/') + newsfeed + str('/'), data=json.dumps(mapping_newsfeed))
        print(response.text)
        # symptom
        response = requests.put(base_url + str('home/_mapping/') + symptom + str('/'), data=json.dumps(mapping_symptom))
        print(response.text)
        # disease
        response = requests.put(base_url + str('home/_mapping/') + disease + str('/'), data=json.dumps(mapping_disease))
        print(response.text)
        # mapping_rehabitation
        response = requests.put(base_url + str('home/_mapping/') + rehabitation + str('/'), data=json.dumps(mapping_rehabitation))
        print(response.text)

        #MASTER
        response = requests.put(base_url + str('master'))
        print(response.text)
        for i in master_list.index_name:
            response = requests.put(base_url + str('master/_mapping/') + i + str('/'), data=json.dumps(mapping_global_master))
            print(response.text)
        # labaccreditationmaster
        response = requests.put(base_url + str('master/_mapping/') + labaccreditationmaster + str('/'), data=json.dumps(mapping_global_master))
        print(response.text)
        # mapping_mater_organisation_branches
        response = requests.put(base_url + str('master/_mapping/') + 'organisation_branches' + str('/'), data=json.dumps(mapping_mater_organisation_branches))
        print(response.text)
        # mapping_mater_lab_branches
        response = requests.put(base_url + str('master/_mapping/') + 'lab_branches' + str('/'), data=json.dumps(mapping_mater_lab_branches))
        print(response.text)

        #GLOBAL
        response = requests.put(base_url + str('global'))
        print(response.text)
        # doctor mapping define
        response = requests.put(base_url + str('global/_mapping/') + doctor + str('/'), data=json.dumps(mapping_doctor))
        print(response.text)
        # organisation mapping
        response = requests.put(base_url + str('global/_mapping/') + organisation + str('/'), data=json.dumps(mapping_organisation))
        print(response.text)
        # lab mapping
        response = requests.put(base_url + str('global/_mapping/') + lab + str('/'), data=json.dumps(mapping_lab))
        print(response.text)
        # pharmacy mapping
        response = requests.put(base_url + str('global/_mapping/') + pharmacy + str('/'), data=json.dumps(mapping_pharmacy))
        print(response.text)
        # bloodbank mapping
        response = requests.put(base_url + str('global/_mapping/') + bloodbank + str('/'), data=json.dumps(mapping_bloodbank))
        print(response.text)
        # bloodbank mapping
        response = requests.put(base_url + str('global/_mapping/') + mapping_ambulance + str('/'), data=json.dumps(mapping_bloodbank))
        print(response.text)

    except Exception as e:
        print
        '%s (%s)' % (e.message, type(e))
    return


####################################################################
# Name - index_data                                                #
# Owner - jitendra dixit
# testing:                                                         #
# Review by -                                                      #
#                                                                  #
####################################################################

import json
from hfu_cms.models import pub_unpub_error_log
from datetime import datetime as ddtt
import datetime

def index_data(index, index_type, doc_id, data):
    #print index_type
    response = True

    data = json.dumps(data)


    #data = {"doctors_category": "111", "news_type_id": 3, "topic_title": "111", "tag_string": "111", "related_topics": "", "newsfeed_html_refined": "<p><strong>Symptom name:</strong> Abdominal Mass</p><p><img alt=\"D:\\Summer Interns Research\\NExt set of images\\abdominal rigidity,  abdominal mass.jpg\" alt_text=\"\" src=\"/media/articles/docx/newsfeed/Abdominal Mass (1) (copy)_1.png\" /></p><p><strong>Description</strong>: </p><p>Abdominal Mass is a condition which results in an unusual/abnormal growth and swelling in the belly/abdomen which alters the shape of the abdomen. A person facing such a condition may witness sudden and unusual weight gain, may feel extremely uncomfortable in the abdomen due to unbearable pain resulting in a bloated belly. Symptoms include sudden swelling, abdominal pain, vomiting, inability to urinate or pass stool, sudden weight gain and belly fullness.</p><p><strong> Causes</strong>:</p><ul><li>Cancer (Colon, Kidney, Liver, Pancreatic, Gall Bladder and Stomach Cancer)</li><li>Inflammatory bowel disease (IBD) </li><li>Enlarged kidney (hydronephrosis)</li><li>Enlarged liver (hepatomegaly)</li><li>Enlarged Spleen (splenomegaly)</li><li>Hernia</li><li>Urinary bladder filled with fluid</li><li>Fluid filled kidney</li><li>Ovarian Cyst</li><li>Viral Infections</li><li>Intestinal obstructions</li><li>Gastrointestinal problems</li></ul><p><strong>Self-Care:</strong></p><ul><li>Regular exercising, like a daily walk or a jog</li><li>Avoid carbonated drinks, alcohol and smoking cigarettes  </li><li>Avoid chewing gums as much as possible</li><li>Eat fruits, vegetables and salads, and keep yourself well hydrated</li><li>Meals at regular intervals </li><li>Avoid over-eating as well as fasting</li><li>On the spot jogging or regular cycling can also benefit one suffering from this condition.</li></ul><p><strong>Disclaimer</strong>:</p>", "newsfeed_image_file_name": "Abdominal Mass (1) (copy)_1.png", "news_type_name": "Health News Feed", "blocked_news": "False", "small_description": "None", "publish_date": "2017-01-11", "id": 1}
    #index_type = 'document'

    try:
        #print "Hi"
        es.index(index = index, doc_type = index_type, id = doc_id, body = data)
    except Exception as e:
        today = ddtt.today()
        # if index_type == 'newsfeed':
        #     news_obj = NewsFeed.objects.get(id=doc_id)
        #     index_type =  news_obj.news_type.name

        publish_date = datetime.date(int(today.year), int(today.month), int(today.day))
        print publish_date, type(publish_date)
        new_record = pub_unpub_error_log(action='Publish',publish_data=data,model_instance_id=int(doc_id),
                                         model_type=index_type,error_message=e.args[2],date_n_time=publish_date)
        new_record.save()

        print e, doc_id
        response = False
    return response


def delete_document(index, index_type, doc_id):
    response = True
    try:
        es.delete(index = index, doc_type = index_type, id = doc_id)

    except Exception as e:
        today = ddtt.today()
        # if index_type == 'newsfeed':
        #     news_obj = NewsFeed.objects.get(id=doc_id)
        #     index_type =  news_obj.news_type.name

        publish_date = datetime.date(int(today.year), int(today.month), int(today.day))
        new_record = pub_unpub_error_log(action='Un-Publish',
                                         model_type=index_type, publish_data={},
                                         model_instance_id=int(doc_id), error_message=e.args[2],date_n_time=publish_date)
        new_record.save()
        print e
        response = False
    return response


def get_all_doc_elastic_ids(request):
    response = True
    try:
        result = es.search(index='global', doc_type='doctor',body= {"query": {"match_all": { }}},size=10000 )
        print("%d documents found" % result['hits']['total'])
        list_ids = []
        for doc in result['hits']['hits']:
            try :
                list_ids.append(int(doc['_id']))
            except:
                print doc
        print "length of list is : ", len(list_ids)
        print list_ids

        from hfu_cms.models import Doctor
        dcms = Doctor.objects.filter(is_disable=False, current_user__username='reenashah', stage_id=5, publish=True)
        listcms =[]
        for d in dcms:
            listcms.append(d.id)
        print "Length of listcms = ", len(listcms)
        for i in listcms:
            if i not in list_ids:
                temp = None
                temp = Doctor.objects.get(id=i)
                print "Missing from Elastic : ", i,"  Name is : ", temp, temp.publish, temp.stage_id, temp.current_user.username

        for i in list_ids :
            if i not in listcms :
                temp = None
                temp = Doctor.objects.get(id=i)
                print "Missing from cms : ", i, "  Name is : ", temp, temp.publish, temp.stage_id, temp.current_user.username



                        # res = es.search(index="test", doc_type="articles", body={"query": {"match": {"content": "fox"}}})
        # print("%d documents found" % res['hits']['total'])
        # for doc in res['hits']['hits']:
        #    print("%s) %s" % (doc['_id'], doc['_source']['content']))

    except Exception as e:
        print e
        response = False
    return HttpResponse(response)