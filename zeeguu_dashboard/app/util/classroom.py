import json

from app.api.api_connection import api_post, api_get


def remove_class(class_id):
    dict = {}
    api_post('remove_cohort/' + str(class_id), dict)


def load_class_info(class_id):
    returned_class_infos_string = api_get("cohort_info/" + str(class_id)).text
    returned_class_info = json.loads(returned_class_infos_string)
    class_info = returned_class_info
    return class_info


def load_classes():
    returned_class_infos_string = api_get("cohorts_info").text
    returned_class_infos = json.loads(returned_class_infos_string)
    classes = returned_class_infos
    return classes


def load_students(class_id):
    returned_student_infos_string = api_get("users_from_cohort/" + str(class_id)).text
    returned_student_infos = json.loads(returned_student_infos_string)
    students = returned_student_infos
    return students


def verify_invite_code_exists(inv_code):
    inv_code_bool = api_get('check_invite_code/' + str(inv_code)).text
    inv_code_bool = json.loads(inv_code_bool)
    if inv_code_bool == 1:
        return False
    return True
