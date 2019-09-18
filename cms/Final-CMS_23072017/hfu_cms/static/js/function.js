Domain = location.protocol + '//' + location.hostname + (location.port ? ':' + location.port : '');


function update() {
    $(".chosen-select").chosen({width: "100%"});
    $('.chosen-select-deselect').chosen({allow_single_deselect: true});
}

$('#category').change(function () {
    if ($(this).val() != '') {
        var formdata = {id: $(this).val()};
        //alert(formdata.id);
        $(".Options").remove();
        // Code commednted during transition from ols SO SPE to new SO SPE finals
        // $.ajax({
        //     type: 'POST', url: Domain + '/doctor/category/', data: formdata, beforeSend: function () {
        //         var text = 'Please wait....';
        //        ajaxindicatorstart(text);
        //     },
        //     success: function (resData) {
        //         ajaxindicatorstop();
        //         resData = JSON.parse(resData);
        //         if (resData.speciality.length > 0 || resData.service.length > 0) {
        //             $('#specialty').empty();
        //             $('#serviceoffer').empty();
        //             var i;
        //             for (i = 0; i < resData.speciality.length; i++) {
        //                 $('#specialty').append(new Option(resData.speciality[i].name, resData.speciality[i].id));
        //             }
        //             $("#specialty").trigger("chosen:updated");
        //             for (i = 0; i < resData.service.length; i++) {
        //                 $('#serviceoffer').append(new Option(resData.service[i].name, resData.service[i].id));
        //             }
        //             $("#serviceoffer").trigger("chosen:updated");
        //
        //         }
        //         else {
        //             $('#specialty').empty();
        //             $('#serviceoffer').empty();
        //             alert("No Specialty and service offer Available for this Category..")
        //         }
        //     },
        //     error: function (e) {
        //         alert(e.message);
        //     }
        // });


        // REPLACEMENT CODE
        //  For Doctor_ServiceOffered_New and Doctor_Speciality_New   --- Start
        //  16 Jan 2018

        $.ajax({
            type: 'POST', url: Domain + '/doctor/category_two/', data: formdata, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.speciality.length > 0 || resData.service.length > 0) {
                    $('#specialty3').empty();
                    $('#serviceoffer3').empty();
                    var i;
                    for (i = 0; i < resData.speciality.length; i++) {
                        $('#specialty3').append(new Option(resData.speciality[i].name, resData.speciality[i].id));
                    }
                    $("#specialty3").trigger("chosen:updated");
                    for (i = 0; i < resData.service.length; i++) {
                        $('#serviceoffer3').append(new Option(resData.service[i].name, resData.service[i].id));
                    }
                    $("#serviceoffer3").trigger("chosen:updated");

                }
                else {
                    $('#specialty3').empty();
                    $('#serviceoffer3').empty();
                    alert("No Doctor_Speciality_New and Doctor_ServiceOffered_New Available for this Category..")
                }
            },
            error: function (e) {
                alert(e.message);
            }
        });


        // For Doctor_ServiceOffered_New and Doctor_Speciality_New   --- End
    }
});

$('#plancatnew').change(function () {
    if ($(this).val() != '') {
        var formdata = {id: $(this).val()};
        $(".Options").remove();
        $.ajax({
            type: 'POST', url: Domain + '/service/plan-new/cat-subcat/', data: formdata, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.subcat.length > 0) {
                    $('#plansubcatnew').empty();
                    var i;
                    $('#plansubcatnew').append(new Option("Select Sub Category", ""));
                    for (i = 0; i < resData.subcat.length; i++) {
                        $('#plansubcatnew').append(new Option(resData.subcat[i].name, resData.subcat[i].id));
                    }
                    $("#plansubcatnew").trigger("chosen:updated");

                }
                else {
                    $('#plansubcatnew').empty();
                    alert("No Plan Sub Category for the plan category selected..")
                }
            },
            error: function (e) {
                alert(e.message);
            }
        });

    }
});

$('#plandetail').change(function () {
    if ($(this).val() != '') {
        var formdata = {id: $(this).val()};
        $(".Options").remove();
        $.ajax({
            type: 'POST', url: Domain + '/service/plan-new/detail-component/', data: formdata, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.component.length > 0) {
                    $('#plancomponent').empty();
                    var i;
                    $('#plancomponent').append(new Option("Select Component", ""));
                    for (i = 0; i < resData.component.length; i++) {
                        $('#plancomponent').append(new Option(resData.component[i].name, resData.component[i].id));
                    }
                    $('#plancomponent').trigger("chosen:updated");

                }
                else {
                    $('#plancomponent').empty();
                    alert("No Plan Component for the plan Details selected..")
                }
            },
            error: function (e) {
                alert(e.message);
            }
        });

    }
});

$('#plancomponent').change(function () {
    if ($(this).val() != '') {
        var formdata = {id: $(this).val()};
        $(".Options").remove();
        $.ajax({
            type: 'POST', url: Domain + '/service/plan-new/component-subcomponent/', data: formdata, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.subcomponent.length > 0) {
                    $('#plansubcomponent').empty();
                    var i;
                    $('#plansubcomponent').append(new Option("Select Sub Component", ""));
                    for (i = 0; i < resData.subcomponent.length; i++) {
                        $('#plansubcomponent').append(new Option(resData.subcomponent[i].name, resData.subcomponent[i].id));
                    }
                    $('#plansubcomponent').trigger("chosen:updated");

                }
                else {
                    $('#plansubcomponent').empty();
                    alert("No Plan Sub Component for the plan Component selected..")
                }
            },
            error: function (e) {
                alert(e.message);
            }
        });

    }
});


//------------------------Filter City on selection of State--- added by jaydeep--------------------------------------//

$('select[name=state_id]').change(function () {
    if ($(this).val() != '') {
        var formdata = {id: $(this).val()};
        $(".Options").remove();
        $.ajax({
            type: 'POST', url: Domain + '/get_city/', data: formdata, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                //alert(resData);
                resData = JSON.parse(resData);
                //alert(resData.speciality[0].id);

                if (resData.city_list.length > 0) {
                    $('select[name=city_id]').empty();
                    $('select[name=locality_id]').empty();
                    $('select[name=locality_idfrom]').empty();
                    $('select[name=locality_idto]').empty();
                    $('select[name=city_id]').append($('<option>', {
                        value: '',
                        text: "--Select City--"
                    }));

                    $('select[name=locality_id]').append($('<option>', {
                        value: '',
                        text: "--Select Location--"
                    }));
                    $('select[name=locality_id]').trigger("chosen:updated");

                    var i;
                    for (i = 0; i < resData.city_list.length; i++) {
                        $('select[name=city_id]').append(new Option(resData.city_list[i].name, resData.city_list[i].id));
                    }

                    $('select[name=locality_idfrom]').append($('<option>', {
                        value: '',
                        text: "--Select Location--"
                    }));
                    $('select[name=locality_idfrom]').trigger("chosen:updated");





                    $('select[name=locality_idto]').append($('<option>', {
                        value: '',
                        text: "--Select Location--"
                    }));
                    $('select[name=locality_idto]').trigger("chosen:updated");




                    $('select[name=city_id]').trigger("chosen:updated");
                    //alert('ok');

                }
                else {
                    $('select[name=city_id]').empty();
                    $('select[name=city_id]').append($('<option>', {
                        value: '',
                        text: "--No City available--"
                    }));
                    $('select[name=city_id]').trigger("chosen:updated");
                    //alert("No City available")
                }
            },
            error: function (e) {
                alert(e.resData.message);
            }

        })

    }
});


///////////////////////////////////////////////////////////////////////////////////////////////////////////
$('select[name=state_id_live]').change(function () {
    if ($(this).val() != '') {
        var formdata = {id: $(this).val()};
        $(".Options").remove();
        $.ajax({
            type: 'POST', url: Domain + '/get_city/', data: formdata, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                //alert(resData);
                resData = JSON.parse(resData);
                //alert(resData.speciality[0].id);

                if (resData.city_list.length > 0) {
                    $('select[name=city_id_live]').empty();
                    $('select[name=locality_id_live_doc]').empty();
                    //$('select[name=locality_idfrom]').empty();
                    //$('select[name=locality_idto]').empty();
                    $('select[name=city_id_live]').append($('<option>', {
                        value: '',
                        text: "--Select City--"
                    }));

                    $('select[name=locality_id_live_doc]').append($('<option>', {
                        value: '',
                        text: "--Select Location--"
                    }));
                    $('select[name=locality_id_live_doc]').trigger("chosen:updated");

                    var i;
                    for (i = 0; i < resData.city_list.length; i++) {
                        $('select[name=city_id_live]').append(new Option(resData.city_list[i].name, resData.city_list[i].id));
                    }

                    // $('select[name=locality_idfrom]').append($('<option>', {
                    //     value: '',
                    //     text: "--Select Location--"
                    // }));
                    // $('select[name=locality_idfrom]').trigger("chosen:updated");





                    // $('select[name=locality_idto]').append($('<option>', {
                    //     value: '',
                    //     text: "--Select Location--"
                    // }));
                    // $('select[name=locality_idto]').trigger("chosen:updated");




                    $('select[name=city_id_live]').trigger("chosen:updated");
                    //alert('ok');

                }
                else {
                    $('select[name=city_id_live]').empty();
                    $('select[name=city_id_live]').append($('<option>', {
                        value: '',
                        text: "--No City available--"
                    }));
                    $('select[name=city_id_live]').trigger("chosen:updated");
                    //alert("No City available")
                }
            },
            error: function (e) {
                alert(e.resData.message);
            }

        })

    }
});




//------------------------Filter Locality on selection of State--- added by jaydeep--------------------------------------//

$('select[name=city_id]').change(function () {
    if ($(this).val() != '') {
        var formdata = {id: $(this).val()};
        $.ajax({
            type: 'POST', url: Domain + '/get_location/', data: formdata, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                //alert(resData);
                ajaxindicatorstop();
                //alert(resData);
                resData = JSON.parse(resData);
                //alert(resData.speciality[0].id);

                if (resData.location_list.length > 0) {
                    $('select[name=locality_id]').empty();
                    $('select[name=locality_id]').append($('<option>', {
                        value: '',
                        text: "--Select Location--"
                    }));
                    var i;
                    for (i = 0; i < resData.location_list.length; i++) {
                        $('select[name=locality_id]').append(new Option(resData.location_list[i].name, resData.location_list[i].id));
                    }
                    $('select[name=locality_id]').trigger("chosen:updated");
                    //alert('ok');
                }
                else {
                    $('select[name=locality_id]').empty();
                    $('select[name=locality_id]').append($('<option>', {
                        value: '',
                        text: "--No Location available--"
                    }));
                    $('select[name=locality_id]').trigger("chosen:updated");
                    //alert("No Location available")
                }


                if (resData.location_list.length > 0) {
                    $('select[name=locality_idfrom]').empty();
                    $('select[name=locality_idfrom]').append($('<option>', {
                        value: '',
                        text: "--Select Location--"
                    }));
                    var i;
                    for (i = 0; i < resData.location_list.length; i++) {
                        $('select[name=locality_idfrom]').append(new Option(resData.location_list[i].name, resData.location_list[i].id));
                    }
                    $('select[name=locality_idfrom]').trigger("chosen:updated");
                    //alert('ok');
                }
                else {
                    $('select[name=locality_idfrom]').empty();
                    $('select[name=locality_idfrom]').append($('<option>', {
                        value: '',
                        text: "--No Location available--"
                    }));
                    $('select[name=locality_idfrom]').trigger("chosen:updated");
                    //alert("No Location available")
                }



                if (resData.location_list.length > 0) {
                    $('select[name=locality_idto]').empty();
                    $('select[name=locality_idto]').append($('<option>', {
                        value: '',
                        text: "--Select Location--"
                    }));
                    var i;
                    for (i = 0; i < resData.location_list.length; i++) {
                        $('select[name=locality_idto]').append(new Option(resData.location_list[i].name, resData.location_list[i].id));
                    }
                    $('select[name=locality_idto]').trigger("chosen:updated");
                    //alert('ok');
                }
                else {
                    $('select[name=locality_idto]').empty();
                    $('select[name=locality_idto]').append($('<option>', {
                        value: '',
                        text: "--No Location available--"
                    }));
                    $('select[name=locality_idto]').trigger("chosen:updated");
                    //alert("No Location available")
                }





            },
            error: function (e) {
                alert(e.resData.message);
            }

        })

    }
});




//////////////////////////////////////////////////////
$('select[name=city_id_live]').change(function () {
    if ($(this).val() != '') {
        var formdata = {id: $(this).val()};
        $.ajax({
            type: 'POST', url: Domain + '/get_location/', data: formdata, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                //alert(resData);
                ajaxindicatorstop();
                //alert(resData);
                resData = JSON.parse(resData);
                //alert(resData.speciality[0].id);

                if (resData.location_list.length > 0) {
                    $('select[name=locality_id_live_doc]').empty();
                    $('select[name=locality_id_live_doc]').append($('<option>', {
                        value: '',
                        text: "--Select Location--"
                    }));
                    var i;
                    for (i = 0; i < resData.location_list.length; i++) {
                        $('select[name=locality_id_live_doc]').append(new Option(resData.location_list[i].name, resData.location_list[i].id));
                    }
                    $('select[name=locality_id_live_doc]').trigger("chosen:updated");
                    //alert('ok');
                }
                else {
                    $('select[name=locality_id_live_doc]').empty();
                    $('select[name=locality_id_live_doc]').append($('<option>', {
                        value: '',
                        text: "--No Location available--"
                    }));
                    $('select[name=locality_id_live_doc]').trigger("chosen:updated");
                    //alert("No Location available")
                }


                // if (resData.location_list.length > 0) {
                //     $('select[name=locality_id_live_doc]').empty();
                //     $('select[name=locality_id_live_doc]').append($('<option>', {
                //         value: '',
                //         text: "--Select Location--"
                //     }));
                //     var i;
                //     // for (i = 0; i < resData.location_list.length; i++) {
                //     //     $('select[name=locality_idfrom]').append(new Option(resData.location_list[i].name, resData.location_list[i].id));
                //     // }
                //     // $('select[name=locality_idfrom]').trigger("chosen:updated");
                //     //alert('ok');
                // }
                // else {
                //     // $('select[name=locality_idfrom]').empty();
                //     // $('select[name=locality_idfrom]').append($('<option>', {
                //     //     value: '',
                //     //     text: "--No Location available--"
                //     // }));
                //     // $('select[name=locality_idfrom]').trigger("chosen:updated");
                //     //alert("No Location available")
                // }



                // if (resData.location_list.length > 0) {
                //     $('select[name=locality_idto]').empty();
                //     $('select[name=locality_idto]').append($('<option>', {
                //         value: '',
                //         text: "--Select Location--"
                //     }));
                //     var i;
                //     for (i = 0; i < resData.location_list.length; i++) {
                //         $('select[name=locality_idto]').append(new Option(resData.location_list[i].name, resData.location_list[i].id));
                //     }
                //     $('select[name=locality_idto]').trigger("chosen:updated");
                //     //alert('ok');
                // }
                // else {
                //     $('select[name=locality_idto]').empty();
                //     $('select[name=locality_idto]').append($('<option>', {
                //         value: '',
                //         text: "--No Location available--"
                //     }));
                //     $('select[name=locality_idto]').trigger("chosen:updated");
                //     //alert("No Location available")
                // }





            },
            error: function (e) {
                alert(e.resData.message);
            }

        })

    }
});





// --------------------------- Get Users Based on stage ---------------------//
$('#stage').change(function () {
    var formdata = {id: $(this).val(),user_type:$('#type_of').val()};

    if (formdata.id != '') {
        $.ajax({
            type: 'POST', url: Domain + '/get/user/', data: formdata, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                //alert(resData);
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                //alert(resData.speciality[0].id);

                if (resData.user_data.length > 0) {
                    $('select[name=users_data]').empty();
                    $('select[name=users_data]').append($('<option>', {
                        value: '',
                        text: "--Select Users--"
                    }));
                    var i;
                    for (i = 0; i < resData.user_data.length; i++) {
                        $('select[name=users_data]').append(new Option(resData.user_data[i].username, resData.user_data[i].id));
                    }
                    $('select[name=users_data]').trigger("chosen:updated");
                    //alert('ok');
                }
                else {
                    $('select[name=users_data]').empty();
                    $('select[name=users_data]').append($('<option>', {
                        value: '',
                        text: "--No Users available--"
                    }));
                    $('select[name=users_data]').trigger("chosen:updated");
                    //alert("No Location available")
                }
            },
            error: function (e) {
                alert("Try Again");
            }

        })

    }
    else {
        alert("Please Select Value")
    }
});


function AddField(x) {
    var formDATA = {};
    var reward = $("#reward_id").val();
    formDATA.Reward = reward;
    formDATA.id = x;
    if (formDATA.Reward) {
        $.ajax({
            type: 'POST', url: Domain + '/reward/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                //alert(resData.length);
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    $('#reward_id').val(null);
                    $('#reward_year').val(null);
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {
                    $('#reward_year').focus();
                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Enter Value");
    }

}

// Add membership
function AddFieldMember(x, y) {
    var formDATA = {};
    var member = $("#member_id").val();
    formDATA.member = member;
    formDATA.id = x;
    formDATA.y = y;
    if (formDATA.member != '') {
        $.ajax({
            type: 'POST', url: Domain + '/reward/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                //alert(resData.length);
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    $('#member_id').val(null);
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {
                    $('#member_id').focus();
                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Enter Value");
    }

}


function AddEducation(x, y) {
    var formDATA = {};
    formDATA.y = y;
    if (formDATA.y == 'edu') {
        var education_id = $("#Education_id").val();
        //alert(year_reward);
        formDATA.education_id = education_id;
        formDATA.id = x;
        if (formDATA.education_id) {  // && formDATA.college && formDATA.year_passing != ''
            $.ajax({
                type: 'POST', url: Domain + '/education/', data: formDATA, beforeSend: function () {
                    var text = 'Please wait....';
                    ajaxindicatorstart(text);
                },
                success: function (resData) {
                    ajaxindicatorstop();
                    resData = JSON.parse(resData);
                    if (resData.Redirect == true) {
                        $('#Education_id').val(null);
                        alert("Done");
                        window.location = resData.RedirectUrl
                    }
                    else {
                        $('#Education_id').focus();
                        alert(resData.Message);
                    }
                }
            });
        }
        else {
            alert("Enter Value");
        }


    }
    else {
        if (formDATA.y == 'exp') {
            var experience_data = $("#Experience_id").val();
            formDATA.id = x;
            formDATA.experience_data = experience_data;
            if (formDATA.experience_data) {  // formDATA.from_year && formDATA.to_year && formDATA.hospital && formDATA.designation != ''
                $.ajax({
                    type: 'POST', url: Domain + '/education/', data: formDATA, beforeSend: function () {
                        var text = 'Please wait....';
                        ajaxindicatorstart(text);
                    },
                    success: function (resData) {
                        ajaxindicatorstop();
                        resData = JSON.parse(resData);
                        if (resData.Redirect == true) {
                            $('#Experience_id').val(null);
                            alert("Done");
                            window.location = resData.RedirectUrl
                        }
                        else {
                            $('#Experience_id').focus();
                            alert(resData.Message);
                        }
                    }
                });
            }
            else {
                alert("Enter Value");
            }


        }
        else {
            if (formDATA.y == 'hospital') {
                var a = undefined;
                var h = $("#h").val();
                var fees = $("#fees").val();
                var email_hospital = $("#email_hospital").val();
                var telephone_hospital = $("#telephone_hospital").val();

                //alert(year_reward);
                formDATA.h = h;
                formDATA.fees = fees;
                formDATA.email_hospital = email_hospital;
                formDATA.telephone_hospital = telephone_hospital;
                formDATA.id = x;
                if (formDATA.h != '') {
                    $.ajax({
                        type: 'POST',
                        url: Domain + '/education/',
                        data: formDATA,
                        beforeSend: function () {
                            var text = 'Please wait....';
                            ajaxindicatorstart(text);
                        },
                        success: function (resData) {
                            ajaxindicatorstop();
                            resData = JSON.parse(resData);
                            if (resData.Redirect == true) {
                                $('#from_year').val(null);
                                $('#to_year').val(null);
                                $('#hospital').val(null);
                                alert("Done");
                                window.location = resData.RedirectUrl
                            }
                            else {
                                $('#from_year').focus();
                                $('#to_year').focus();
                                alert(resData.Message);
                            }
                        }
                    });
                }
                else {
                    alert("Enter Value");
                }

            }
            else {
                if (formDATA.y == 'clinic') {
                    var c = $("#c").val();
                    var fees = $("#fees").val();
                    var email_clinic = $("#email_clinic").val();
                    var telephone_clinic = $("#telephone_clinic").val();
                    //alert(year_reward);
                    formDATA.c = c;
                    formDATA.fees = fees;
                    formDATA.email_clinic = email_clinic;
                    formDATA.telephone_clinic = telephone_clinic;
                    formDATA.id = x;
                    if (formDATA.c != '') {
                        $.ajax({
                            type: 'POST',
                            url: Domain + '/education/',
                            data: formDATA,
                            beforeSend: function () {
                                var text = 'Please wait....';
                                ajaxindicatorstart(text);
                            },
                            success: function (resData) {
                                ajaxindicatorstop();
                                resData = JSON.parse(resData);
                                if (resData.Redirect == true) {
                                    $('#c').val(null);
                                    $('#fees').val(null);
                                    $('#email_clinic').val(null);
                                    $('#telephone_clinic').val(null);
                                    alert("Done");
                                    window.location = resData.RedirectUrl
                                }
                                else {
                                    $('#c').focus();
                                    $('#email_clinic').focus();
                                    alert(resData.Message);
                                }
                            }
                        });
                    }
                    else {
                        alert("Enter Value");
                    }

                }
                else {
                    if (formDATA.y == 'organisation') {
                        var c = $("#c").val();
                        var fees = $("#fees").val();
                        var email_clinic = $("#email_organisation").val();
                        var telephone_clinic = $("#telephone_clinic").val();
                        //alert(year_reward);
                        formDATA.c = c;
                        formDATA.fees = fees;
                        formDATA.email_clinic = email_clinic;
                        formDATA.telephone_clinic = telephone_clinic;
                        formDATA.id = x;
                        if (formDATA.c != '') {
                            $.ajax({
                                type: 'POST',
                                url: Domain + '/education/',
                                data: formDATA,
                                beforeSend: function () {
                                    var text = 'Please wait....';
                                    ajaxindicatorstart(text);
                                },
                                success: function (resData) {
                                    ajaxindicatorstop();
                                    resData = JSON.parse(resData);
                                    if (resData.Redirect == true) {
                                        $('#c').val(null);
                                        $('#fees').val(null);
                                        $('#email_organisation').val(null);
                                        $('#telephone_clinic').val(null);
                                        alert("Done");
                                        window.location = resData.RedirectUrl
                                    }
                                    else {
                                        $('#c').focus();
                                        $('#email_organisation').focus();
                                        alert(resData.Message);
                                    }
                                }
                            });
                        }
                        else {
                            alert("Enter Value");
                        }

                    }

                }

            }
        }
    }


}


// Delete functionality
function Delete(z, x, y) {
    var formDATA = {};
    formDATA.id = x;
    formDATA.y = y;
    formDATA.d = z;
    if (formDATA.y == "organisation") {
        if (formDATA.id && formDATA.y && formDATA.d != '') {
            $.ajax({
                type: 'POST', url: Domain + '/delete/', data: formDATA, beforeSend: function () {
                    var text = 'Please wait....';
                    ajaxindicatorstart(text);
                },
                success: function (resData) {
                    ajaxindicatorstop();
                    resData = JSON.parse(resData);
                    if (resData.Redirect == true) {
                        alert(resData.Message);
                        window.location = resData.RedirectUrl;
                    }
                    else {

                        alert(resData.Message);
                    }
                }
            });
        }
        else {
            alert("Something bad happened");
        }

    }
    else {
        if (formDATA.y == "hospital") {
            if (formDATA.id && formDATA.y && formDATA.d != '') {
                $.ajax({
                    type: 'POST', url: Domain + '/delete/', data: formDATA, beforeSend: function () {
                        var text = 'Please wait....';
                        ajaxindicatorstart(text);
                    },
                    success: function (resData) {
                        ajaxindicatorstop();
                        resData = JSON.parse(resData);
                        if (resData.Redirect == true) {
                            alert(resData.Message);
                            window.location = resData.RedirectUrl;
                        }
                        else {

                            alert(resData.Message);
                        }
                    }
                });
            }
            else {
                alert("Something bad happened");
            }

        }
        else {
            if (formDATA.y == "edu") {
                if (formDATA.id && formDATA.y && formDATA.d != '') {
                    $.ajax({
                        type: 'POST',
                        url: Domain + '/delete/',
                        data: formDATA,
                        beforeSend: function () {
                            var text = 'Please wait....';
                            ajaxindicatorstart(text);
                        },
                        success: function (resData) {
                            ajaxindicatorstop();
                            resData = JSON.parse(resData);
                            if (resData.Redirect == true) {
                                alert(resData.Message);
                                window.location = resData.RedirectUrl;
                            }
                            else {

                                alert(resData.Message);
                            }
                        }
                    });
                }
                else {
                    alert("Something bad happened");
                }

            }
            else {
                if (formDATA.y == "exp") {
                    if (formDATA.id && formDATA.y && formDATA.d != '') {
                        $.ajax({
                            type: 'POST',
                            url: Domain + '/delete/',
                            data: formDATA,
                            beforeSend: function () {
                                var text = 'Please wait....';
                                ajaxindicatorstart(text);
                            },
                            success: function (resData) {
                                ajaxindicatorstop();
                                resData = JSON.parse(resData);
                                if (resData.Redirect == true) {
                                    alert(resData.Message);
                                    window.location = resData.RedirectUrl;
                                }
                                else {

                                    alert(resData.Message);
                                }
                            }
                        });
                    }
                    else {
                        alert("Something bad happened");
                    }

                }
                else {
                    if (formDATA.y == "reward") {
                        if (formDATA.id && formDATA.y && formDATA.d != '') {
                            $.ajax({
                                type: 'POST',
                                url: Domain + '/delete/',
                                data: formDATA,
                                beforeSend: function () {
                                    var text = 'Please wait....';
                                    ajaxindicatorstart(text);
                                },
                                success: function (resData) {
                                    ajaxindicatorstop();
                                    resData = JSON.parse(resData);
                                    if (resData.Redirect == true) {
                                        alert(resData.Message);
                                        window.location = resData.RedirectUrl;
                                    }
                                    else {

                                        alert(resData.Message);
                                    }
                                }
                            });
                        }
                        else {
                            alert("Something bad happened");
                        }

                    }
                    else {
                        if (formDATA.y == "member") {
                            if (formDATA.id && formDATA.y && formDATA.d != '') {
                                $.ajax({
                                    type: 'POST',
                                    url: Domain + '/delete/',
                                    data: formDATA,
                                    beforeSend: function () {
                                        var text = 'Please wait....';
                                        ajaxindicatorstart(text);
                                    },
                                    success: function (resData) {
                                        ajaxindicatorstop();
                                        resData = JSON.parse(resData);
                                        if (resData.Redirect == true) {
                                            alert(resData.Message);
                                            window.location = resData.RedirectUrl;
                                        }
                                        else {

                                            alert(resData.Message);
                                        }
                                    }
                                });
                            }
                            else {
                                alert("Something bad happened");
                            }

                        }

                    }

                }


            }

        }
    }
}

// Added by Jaydeep.........//
//$(function () {
//    $("#acceptance_date").datepicker({dateFormat: 'dd-mm-yy'});
//    //$("#from_year").datepicker({dateFormat: 'yy-mm-dd'});
//    //$("#to_year").datepicker({dateFormat: 'yy-mm-dd'});
//    //$("#college_year").datepicker({dateFormat: 'yy-mm-dd'});
//    //$("#dob").datepicker({dateFormat: 'yy-mm-dd'});
//
//});


$(function () {


    $(".chosen-select").chosen({width: "100%"});
    $('.chosen-select-deselect').chosen({allow_single_deselect: true});
});


// By vishnu

// Assignment functionality
function Assign() {
    //var checkedValues = [];
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/assign/doctor/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            },
            error: function(resData){
                alert("Try Again")
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }


}



// News Assignment
function AssignNews() {
    //var checkedValues = [];
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/news-feed/assign/set/global/assign/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            },
            error: function(resData){
                alert("Try Again")
            }
        });
    }
    else {
        alert("Please select Stage,User and News");
    }


}

// Wellnes news assignment

function AssignWellnessNews() {
    //var checkedValues = [];
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/news-feed/assign/set/wellness/assign/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            },
            error: function(resData){
                alert("Try Again")
            }
        });
    }
    else {
        alert("Please select Stage,User and News");
    }


}



// Wellnes news assignment

function AssignHealthNews() {
    //var checkedValues = [];
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/news-feed/assign/set/health/assign/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            },
            error: function(resData){
                alert("Try Again")
            }
        });
    }
    else {
        alert("Please select Stage,User and News");
    }


}




// Organisation Assignment
function AssignOrganisation() {
    //var checkedValues = [];
    alert("This is Organisation Assignment");
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/assign/organisation/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }

}


// Lab Assignment
function AssignLab() {
    //var checkedValues = [];
    // alert("This is Lab Assignment");
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/assign/lab/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }

}


function PostAssignment() {
    var reviewer = $("#reviewer").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();
    var formDATA = {};
    formDATA.reviewer = reviewer;
    formDATA.newstype = $('#newstype').val();
    formDATA.checkedValues = checkedValues;
    if (formDATA.reviewer && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/cms/content/assign/',
            data: formDATA,
            beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Reviewer and News");
    }


}


function PlanAssignment() {
    var reviewer = $("#reviewer").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();
    var formDATA = {};
    formDATA.reviewer = reviewer;
    formDATA.servicetype = $('#servicetype').val();
    formDATA.checkedValues = checkedValues;
    if (formDATA.reviewer && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/cms/plan/assign/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {
                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Reviewer and Plans");
    }


}


function PublishNewsToApp(id) {
    var newsType = $("#newsType").val();
    var mode = $("#mode").val();
    if (id != null || id != '' || newsType != null || newsType != '' || mode != null || mode != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/cms/content/publish/',
            data: {id: id, newsType: newsType, mode: mode},
            beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Error occurred");
    }


}


function PublishPlansToApp(id, servicetype) {
    var mode = $("#mode").val();
    if (id != null || id != '' || servicetype != null || servicetype != '' || mode != null || mode != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/cms/plan/publish/',
            data: {id: id, servicetype: servicetype, mode: mode},
            beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {
                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Error occurred");
    }
}

//*********************************added by Jaydeep ****************************************//

function PublishProviderToApp(id, servicetype) {
    alert('called');
    var mode = $("#mode").val();
    if (id != null || id != '' || servicetype != null || servicetype != '' || mode != null || mode != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/cms/provider/publish/',
            data: {id: id, servicetype: servicetype, mode: mode},
            beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {
                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Error occurred");
    }
}


function Publish(x) {
    var formDATA = {};
    formDATA.x = x;
    if (formDATA.x != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/publish/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Something bad happened");
    }


}


function PDF_creation(x) {
    var formDATA = {};
    formDATA.unique_id = x;
    if (formDATA.unique_id != '') {
        var url = Domain + '/doctor/create_pdf/?unique_id=' + formDATA.unique_id + '';
        var win = window.open(url, '_blank');
        win.focus();
        //$.ajax({
        //    type: 'POST', url: Domain + '/doctor/create_pdf/', data:{unique_id:formDATA.unique_id, csrfmiddlewaretoken: '{{ csrf_token }}'}, beforeSend: function(){
        //      var text = 'Please wait....';
        //        ajaxindicatorstart(text);
        //    },
        //    success: function (resData) {
        //        ajaxindicatorstop();
        //        //resData = JSON.parse(resData);
        //        //if (resData.Redirect == true) {
        //        //    alert(resData.Message);
        //        //    window.location = resData.RedirectUrl;
        //        //}
        //        //else {
        //        //
        //        //    alert(resData.Message);
        //        //}
        //    }
        //});
    }
    else {
        alert("Something bad happened");
    }


}


function Send(x) {
    var formDATA = {};
    formDATA.x = x;
    //alert("This Functionality Under Process");
    //return false;
    if (formDATA.x != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/create/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Something bad happened");
    }

}

function SendMaster() {
    var formDATA = {};
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();
    formDATA.type = $('#master_type').val();
    formDATA.checkedValues = checkedValues;
    //alert("This Functionality Under Process");
    //return false;
    if (formDATA.checkedValues != '' && formDATA.type != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/master/erp/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Something bad happened");
    }

}

function Revert(x) {
    var formDATA = {};
    var revert_comment = document.getElementById('revert_comment').value;
    formDATA.x = x;
    formDATA.revert_comment = revert_comment;
    if (formDATA.x != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/revert/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Something bad happened");
    }


}

function DeleteSchedule(d, hc, sc, x) {

    var formDATA = {};
    formDATA.d = d;
    formDATA.hc = hc;
    formDATA.sc = sc;
    formDATA.x = x;

    if (formDATA.x != '') {
        $.ajax({
            type: 'POST', url: Domain + '/schedule/delete/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Something bad happened");
    }

}

function ajaxindicatorstart(text) {
    if (jQuery('#popup-inner').find('#resultLoading').attr('id') != 'resultLoading') {
        jQuery('#popup-inner').append('<div id="resultLoading" style="display:none"><div><img src="' + "/static" + '/image/ajax-loaders/ajax-loader-8.gif"><div>' + text + '</div></div><div class="bg"></div></div>');
    }

    jQuery('#resultLoading').css({
        'width': '100%',
        'height': '100%',
        'position': 'fixed',
        'z-index': '10000000',
        'top': '0',
        'left': '0',
        'right': '0',
        'bottom': '0',
        'margin': 'auto'
    });

    jQuery('#resultLoading .bg').css({
        'background': '#000000',
        'opacity': '0.7',
        'width': '100%',
        'height': '100%',
        'position': 'absolute',
        'top': '0'
    });

    jQuery('#resultLoading>div:first').css({
        'width': '250px',
        'height': '75px',
        'text-align': 'center',
        'position': 'fixed',
        'top': '0',
        'left': '0',
        'right': '0',
        'bottom': '0',
        'margin': 'auto',
        'font-size': '16px',
        'z-index': '10',
        'color': '#ffffff'

    });

    jQuery('#resultLoading .bg').height('100%');
    jQuery('#resultLoading').fadeIn(300);
    jQuery('body').css('cursor', 'wait');
}

function ajaxindicatorstop() {
    jQuery('#resultLoading .bg').height('100%');
    jQuery('#resultLoading').fadeOut(300);
    jQuery('body').css('cursor', 'default');
    return false;
}
/*This Function is Used  For Hospital Address*/
// hospital address
$('#h').change(function () {
    if ($(this).val() != '') {
        var formdata = {id: $(this).val()};
        //$(".Options").remove();
        $.ajax({
            type: 'GET', url: Domain + '/organisation/address/', data: formdata, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);

                if (resData.address.length > 0) {
                    for (var i = 0; i < resData.address.length; i++) {
                        $('#street').val(resData.address[i].street);
                        $('#city').val(resData.address[i].city__name);
                        $('#state').val(resData.address[i].state__name);
                        $('#pin').val(resData.address[i].pincode);
                        $('#locality').val(resData.address[i].locality__name);
                        $('#email_organisation').val(resData.address[i].email);
                        $('#telephone_clinic').val(resData.address[i].emergency_no);
                        if (resData.address[i].is_hospital) {
                            $('#type').val("Hospital");
                        }
                        if (resData.address[i].is_clinic) {
                            $('#type').val("Clinic");
                        }
                    }
                    //alert(resData.Message);
                    //window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
});
//// Organisation address
//$('#c').change(function () {
//    if ($(this).val() != '') {
//        var formdata = {id: $(this).val()};
//        //$(".Options").remove();
//        $.ajax({
//            type: 'GET', url: Domain + '/organisation/address/', data: formdata, beforeSend: function () {
//                var text = 'Please wait....';
//                ajaxindicatorstart(text);
//            },
//            success: function (resData) {
//                ajaxindicatorstop();
//                //alert(resData);
//                resData = JSON.parse(resData);
//                if (resData.address.length > 0) {
//                    for (var i = 0; i < resData.address.length; i++) {
//                        $('#street').val(resData.address[i].street);
//                        $('#city').val(resData.address[i].city__name);
//                        $('#state').val(resData.address[i].state__name);
//                        $('#pin').val(resData.address[i].pincode);
//                        $('#locality').val(resData.address[i].locality__name);
//                        $('#email_organisation').val(resData.address[i].email);
//                        $('#telephone_clinic').val(resData.address[i].emergency_no);
//                        if (resData.address[i].is_hospital) {
//                            $('#type').val("Hospital");
//                        }
//                        if (resData.address[i].is_clinic) {
//                            $('#type').val("Clinic");
//                        }
//
//
//                    }
//                    //alert(resData.Message);
//                    //window.location = resData.RedirectUrl;
//                }
//                else {
//
//                    alert(resData.Message);
//                }
//            }
//        });
//    }
//});


//-------------------------Added by Jaydeep----------------------------------------------------------//

function settablevalue(planId) {
    if (planId == null) {
        alert("Please First of all Save Plan Category and Plan Name at least..!!");
    }
    else {
        var test = $('#maintable').find('input.serviceoffered').val();
        //alert(test);
        var i;
        var tabledata = {};
        var tabledata_array = [];
        $('#maintable').find('tr.plandetailrows').each(function (i, row) {
            // reference all the stuff you need first
            tabledata = {};
            var $row = $(row);
            tabledata.serviceoffer = $row.find('input.serviceoffered').val();
            tabledata.desc = $row.find('input.description').val();
            tabledata_array.push(tabledata);
            console.log(JSON.stringify(tabledata_array));
            //console.log(JSON.parse(JSON.stringify(tabledata_array)))
        });
        var data = {};
        data.serviceofferlist = JSON.stringify(tabledata_array);
        data.planId = planId;
        $.ajax({
            type: 'POST',
            url: Domain + '/cms/plans/add_edit_plan_details/',
            data: data,
            beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                alert(resData.Message)
            }
        });

    }
}


//------------------------add_edit_service_provider form Validation start------------------------------------------//


//------------------------add_edit_service_plan form Validation start------------------------------------------//

$("#plan_price").focusout(function () {
    var plan_price = $('#plan_price').val();
    var discount = $('#discount_on_plan').val();
    if (plan_price > 0) {
        var effective_price = plan_price - (plan_price * discount) / 100;
        var effective_value = document.getElementById("price_of_plan_after_discount");
        effective_value.value = effective_price;
    }
    else if (plan_price < 0) {
        var effective_value = document.getElementById("price_of_plan_after_discount");
        alert("Plan Price is not possible in Negative...");
        effective_value.value = 0;
    }

});

$("#discount_on_plan").focusout(function () {
    var discount = $('#discount_on_plan').val();
    var plan_price = $('#plan_price').val();
    if (discount > 100) {
        alert("Discount is possible only up to 100%..");
        $("#discount_on_plan").val("");
        $('#discount_on_plan').focus();
    }

    if (plan_price > 0) {
        if (discount <= 100) {
            var effective_price = plan_price - (plan_price * discount) / 100;
            var effective_value = document.getElementById("price_of_plan_after_discount");
            effective_value.value = effective_price;
        }
        else {
            var effective_price = plan_price;
            var effective_value = document.getElementById("price_of_plan_after_discount");
            effective_value.value = effective_price;
        }

    }
    else if (plan_price < 0) {
        var effective_value = document.getElementById("price_of_plan_after_discount");
        alert("Plan Price is not possible in Negative...");
        effective_value.value = 0;
    }
});


$("#plan_duration").on('keyup', function (e) {
    var val = $(this).val();
    if (val.match(/[^\d+(?:\.\d+|)$]/g)) {
        alert("Please Enter Only Numeric Values...Not Character Like This: " + "'" + val + "'");
        $(this).val(val.replace(/[^\d+(?:\.\d+|)$]/g, ''));
    }
});

$("#plan_price").on('keyup', function (e) {
    var val = $(this).val();
    if (val.match(/[^\d+(?:\.\d+|)$]/g)) {
        alert("Please Enter Only Numeric Values...Not Character Like This: " + "'" + val + "'");
        $(this).val(val.replace(/[^\d+(?:\.\d+|)$]/g, ''));
    }
});
$("#discount_on_plan").on('keyup', function (e) {
    var val = $(this).val();
    if (val.match(/[^\d+(?:\.\d+|)$]/g)) {
        alert("Please Enter Only Numeric Values...Not Character Like This: " + "'" + val + "'");
        $(this).val(val.replace(/[^\d+(?:\.\d+|)$]/g, ''));
    }
});
$("#plan_title").on('keyup', function (e) {
    var val = $(this).val();
    if (val.match(/[^a-zA-Z0-9 _]/g)) {
        alert("Please Enter Only Characters and Numbers combination not special characters like : @,#,$,%,^,&,*");
        $(this).val(val.replace(/[^a-zA-Z0-9 _]/g, ''));
    }
});
$("#plan_name").on('keyup', function (e) {
    var val = $(this).val();
    if (val.match(/[^a-zA-Z0-9 _]/g)) {
        alert("Please Enter Only Characters and Numbers combination not special characters like : @,#,$,%,^,&,*");
        $(this).val(val.replace(/[^a-zA-Z0-9 _]/g, ''));
    }
});


//
//------------------------add_edit_service_plan form Validation End------------------------------------------//
// Assignment Search Doctor
function SearchDoctorAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/search/doctor/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}

// Search global News data
function SearchGlobalNewsAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/news-feed/search-news/global/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}

// Search Wellness News data
function SearchWellnessNewsAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/news-feed/search-news/wellness/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}


// Search health News data
function SearchHealthNewsAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/news-feed/search-news/health/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}

// Assign search organisation
// Assignment Search Doctor
function SearchOrganisationAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/organisation/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}


// Assignment Search lab
function SearchLabAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/lab/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}

// Assignment Search Lab
function SearchLabOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/lab/assign/search_lab_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}
//Search Doctor caller and reviewer
function SearchDoctor(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $('#ser').removeAttr('selected');
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/doctor/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}

// Search Doctor by admin
function SearchDoctorAdmin() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/doctor/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });
}


// Search Doctor by admin
function SearchDoctorAssociationUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/organisation/association/user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('#jd').replaceWith(data);
        },
        error: function(data){
            alert("check Internet connection")
        }

    });
}
//Search Doctor on Stage

function SearchDoctorAdminOnStageUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/doctor/assign/search_doctor_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });
}


//service offered search
function SearchServiceOffered() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain +'/search/service_offered/search_service_offered/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });
}
// By Doctor users Searchs
function SearchDoctorAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/doctor/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}

// Search By Statges
function SearchDoctorAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/doctor/by/stages/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert('Something Bad Happened');
                location.reload();
            }

        });
    }
    else {
        alert("Please select at least one stage")
    }


}


// Search Organisation by admin
function SearchOrganisationAdmin() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    formDATA.q2 = $("#utype").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/organisation/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}

// Search organisation by stage Admin

function SearchOrganisationAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/organisation/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}

// Search organisation by users Admin

function SearchOrganisationAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/organisation/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}


// Search lab by users Admin

function SearchLabAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/lab/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}

// Search organisation by stage Admin

function SearchLabAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    alert(formDATA.q)
    $.ajax({
        type: 'POST',
        url: Domain + '/search/lab/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}

// Search Doctor by publisher
function SearchDoctorByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/doctor/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}

// Search Global news by publisher
function SearchGlobalNewsByPublisher(v, t) {
    var formDATA = {};
    formDATA.q = v;
    formDATA.t = t;
    if (formDATA.q != '' && formDATA.t != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/news-feed/publish/global-search/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}

// Search Global news by publisher
function SearchHealthNewsByPublisher(v, t) {
    var formDATA = {};
    formDATA.q = v;
    formDATA.t = t;
    if (formDATA.q != '' && formDATA.t != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/news-feed/publish/global-search/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}

function SearchOrganisationByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/organisation/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}

function doctorDeAssociationWithOrganisation(id) {
    $.ajax({
        type: 'GET',
        url: Domain + '/delete/organisation/association_doctor/?id=' + id,
        data: {csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {

        },
        error: function (data) {

        }

    });
}

function SearchOrganisation(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/organisation/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });
}


// Search lab by publisher
function SearchlabByPublisher(v) {
    var formDATA = {};
    formDATA.q = v
    ;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/lab/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}



// View Questions By Assignment
function SearchQuestionsByType(v) {
    var formDATA = {};
    formDATA.q = v
    ;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/question/by/type/admin/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}


// View Feedback By Status
function SearchFeedbackByStatus(v) {
    var formDATA = {};
    formDATA.q = v
    ;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/feedback/by/status/admin/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }
}





// Search blood bank by publisher
function SearchbloodbankByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/blood_bank/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}


// Search ambulance by publisher
function SearchambulanceByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/ambulance/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}



// Search pharmacy by publisher
function SearchpharmacyByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/pharmacy/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert(data)
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}



function SearchLab(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/lab/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });
}

//Check User name is available
function checkUserName() {
    var formData = {};
    formData.user_name = $("#user_name").val();

    if (formData.user_name != "") {
        $.ajax({
            type: 'POST',
            url: Domain + '/hfu/cms/check/username/',
            data: {formData: formData.user_name, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                if (data == 'False') {
                    $("#not_valid").replaceWith('<span class="text-danger" id="not_valid">This User name is not available</span>');
                    $("#user_name").focus().val('');
                    //location.reload();
                }
                else {
                    $("#not_valid").replaceWith('<span class="text-success" id="not_valid">This User name is available</span>');
                }
                //$('div.table-responsive').replaceWith(data);
            }

        })
    }
    else {
        return false;
    }

}

function organisation_move_to_next_stage() {
    var formData = {};
    formData.publisher_name = $("#publisher_name").val();
    formData.organisation_id = $("#organisation_id").val();
    formData.validator_id = $("#validator_id").val();
    formData.csrfmiddlewaretoken = '{{ csrf_token }}';
    $("#add_data_un_publish").html('');
    if (formData.organisation_id != "" && formData.publisher_name) {
        $.ajax({
            type: 'POST',
            url: Domain + '/mark/complete/organisation/publisher/',
            data: formData,
            success: function (data) {
                data = JSON.parse(data);
                if (data.status == 'Fail' && data.data) {
                    $('#myModal').modal('show');
                    var str = "<h4 style='color: red'>" + data.message + "</h4> <div class='table-responsive table_modify_for_all p_tb_10'> <table class='table table-bordered m_b_0'> <thead class='bg_ededed'> <tr> <th>Sr.No.</th> <th>Doctor Name</th> <th>Zone</th> <th>Zone Location</th> <th>Category</th> <th>Speciality</th><th>Registration No.</th> </tr> </thead><tbody>";

                    for (var i = 0; i < data.data.length; i++) {
                        var counter = i + 1;
                        str = str + "<tr><td>" + counter + "</td><td>" + data.data[i].name + "</td><td>" + data.data[i].zone + "</td><td>" + data.data[i].zone_location + "</td><td>" + data.data[i].category + "</td><td>" + data.data[i].speciality + "</td><td>" + data.data[i].registration_data + "</td></tr>";
                    }
                    str += "</tbody></table></div>";
                    $("#add_data_un_publish").html(str)


                }
                else if (data.status == "Fail") {
                    alert(data.message)
                }
                else if (data.status == "Ok") {
                    alert(data.message);
                    location.reload();
                }
                //$('div.table-responsive').replaceWith(data);
            }

        })
    }
    else {
        return false;
    }
}


function doctor_move_to_next_stage() {
    $("#add_data_un_publish_doctor").html('');
    var formData = {};
    formData.publisher_name = $("#publisher_name").val();
    formData.doctor_id = $("#doctor_id").val();
    formData.validator_id = $("#validator_name").val();
    if($("#live_doc_true").val()){
       formData.live_doc_true = $("#live_doc_true").val();
    }

    formData.csrfmiddlewaretoken = '{{ csrf_token }}';

    if (formData.doctor_id != "" && formData.publisher_name && formData.validator_id) {
        $.ajax({
            type: 'POST',
            url: Domain + '/mark/complete/doctor/publisher/',
            data: formData,
            success: function (data) {
                data = JSON.parse(data);
                if (data.status == 'Fail' && data.data) {
                    $('#myModal_doctor').modal('show');
                    var str = "<h4 style='color: red'>" + data.message + "</h4> <div class='table-responsive table_modify_for_all p_tb_10'> <table class='table table-bordered m_b_0'> <thead class='bg_ededed'> <tr> <th>Sr.No.</th> <th>Doctor Name</th> <th>Address</th> <th>Locality</th> <th>City</th>  </tr> </thead><tbody>";

                    for (var i = 0; i < data.data.length; i++) {
                        var counter = i + 1;
                        str = str + "<tr><td>" + counter + "</td><td>" + data.data[i].name + "</td><td>" + data.data[i].address + "</td><td>" + data.data[i].locality + "</td><td>" + data.data[i].city + "</td></tr>";
                    }
                    alert(str)
                    str += "</tbody></table></div>";
                    $("#add_data_un_publish_doctor").html(str)

                }
                else if (data.status == "Fail") {
                    alert(data.message)
                }
                else if (data.status == "Ok") {
                    alert(data.message);
                     if($("#live_doc_true").val()){
                        window.location.href = Domain + '/live-doctor/listing/new-registrations/'
                    }else {
                          window.location.href = Domain + '/doctor/listing/'
                     }

                }

                //$('div.table-responsive').replaceWith(data);
            }

        })
    }
    else {
        return false;
    }
}


// ajax file upload function


function add_pagination(page) {
    var url = window.location.href;
    alert(url);
    if (url.indexOf('&page') > -1) {
        var urlArray = url.split('&page');
        url = urlArray[0];
    }
    else if (url.indexOf('page') > -1) {
        var urlArray = url.split('page');
        url = urlArray[0];
    }
    var separator = (url.indexOf("?") === -1) ? "?" : "&";
    var newParam = separator + 'page=';
    var newUrl = url.replace(newParam, "");
    newUrl += newParam + page;
    window.location.href = newUrl;

}

// ajax file upload function

function fileUploadAjax() {
    var formdata = new FormData();
    $.each($('#upload-photo')[0].files, function (i, file) {
        formdata.append('poster', file);
    });
    alert(formdata);
    $.ajax({
        url: "/api/upload_image/",
        data: formdata,
        dataType: "json",
        type: "post",
        cache: false,
        contentType: false,
        processData: false,
        success: function (data) {
            $('#pre_img').attr('src', '/static' + data.url);
            $('#pre_imginp').val('/static' + data.url)
        },
        failure: function () {
            $(this).addClass("error");
        }
    });
    return false
}


//----------------BLOODBANK SEARCHES-------------


// Assignment Search Blood Bank added by Nishank
function SearchBloodBankOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/blood-bank/assign/search_bloodbank_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},


        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert(formDATA.q)
            alert("Check your Internet connection")
        }

    });
    }
// Assignment Search Bloodbank by Nishank
function SearchBloodBankAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/blood-bank/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}

// Bloodbank Assignment by Nishank
function AssignBloodBank() {
    //var checkedValues = [];
    // alert("This is Bloodbank Assignment");
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();


    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
             }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;


    formDATA.checkedValues = checkedValues;

    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/assign/bloodbank/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                //alert("resData");
                //alert(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                                              }
                else {

                    alert(resData.Message);
                     }
                                        }
               });
                                                                               }
    else {

        alert("Please select Stage,User and Bloodbanks");
         }

                                }


// search blood bank by stages
function SearchBloodBankAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/blood-bank/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}


function SearchBloodbank(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/blood-bank/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });
}

//for correct by users
function SearchBloodbankAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/bloodbank/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}

//-------------AMBULANCE SEARCHES------------

// Assignment Search lab
function SearchAmbulanceAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/search/ambulance/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}


function SearchAmbulanceAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/ambulance/by/users/',

            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert(" console.log(url) Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}




// Assignment Search Ambulance added by Nishank
function SearchAmbulanceOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/ambulance/assign/search_ambulance_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });
    }



// Assignment Search Ambulance by Nishank
function SearchaAmbulanceAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/ambulance/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}

// Ambulance Assignment by Nishank
function AssignAmbulance() {
    //var checkedValues = [];

    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
                                                                    }
                                                       ).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/assign/ambulance/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                                              }
                else {

                    alert(resData.Message);
                     }
                                        }
               });
                                                                               }
    else {
        alert("Please select Stage,User and Ambulances");
         }

                                }


// search ambulance by stages
function SearchAmbulanceAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/ambulance/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}


function SearchAmbulance(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/ambulance/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });
}

//   PHARMACY FUNCTIONS

// Search Pharmacy by users Admin

function SearchPharmacyAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;

    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/pharmacy/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}



// Assignment Search Pharmacy
function SearchPharmacyOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/pharmacy/assign/search_pharmacy_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}

// Search Pharmacy by stage Admin

function SearchPharmacyAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/pharmacy/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}


// Assignment Search pharmacy
function SearchPharmacyAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/pharmacy/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}


// Pharmacy Assignment
function AssignPharmacy() {
    //var checkedValues = [];
    // alert("This is Lab Assignment");
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/assign/pharmacy/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }

}


function SearchPharmacy(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/pharmacy/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Please check your internet connection")
        }

    });
}

//DISEASE FUNCTIONS

// Assignment Search disease
function SearchDiseaseOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/search/disease/assign/search_disease_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}

// Search Disease by stage Admin

function SearchDiseaseAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/disease/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}

// Disease Assignment
function AssignDisease() {
    //var checkedValues = [];
    // alert("This is Lab Assignment");
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/assign/disease/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }

}


// Assignment Search disease
function SearchDiseaseAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/disease/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}

function SearchDisease(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/disease/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
           alert("Please check your Internet Connection");
        }


    });
}



//drug FUNCTIONS

// Assignment Search drug
function SearchDrugOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/drug/assign/search_drug_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}

// Search drug by stage Admin

function SearchDrugAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/drug/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}


// drug Assignment
function AssignDrug() {
    //var checkedValues = [];
    // alert("This is Disease Assignment");
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/assign/drug/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }

}

function SearchDrug(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/drug/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });
}



// Assignment Search drug
function SearchDrugAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/drug/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });
}





//symptoms FUNCTIONS

// Assignment Search symptoms
function SearchSymptomsOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/symptoms/assign/search_symptoms_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}


// Search symptoms by stage Admin

function SearchSymptomsAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/symptoms/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }
    });


}

// symptoms Assignment
function AssignSymptoms() {
    //var checkedValues = [];
    // alert("This is Symptom Assignment");
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();
    alert(telecaller);
    alert(stage);

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    alert( checkedValues);
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/assign/symptoms/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }

}

// Assignment Search symptoms
function SearchSymptomsAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/symptoms/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}


function SearchSymptoms(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/symptoms/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
           alert("Please check your Internet Connection");
        }

    });
}




// Home Plan Search
function SearchHomeplanOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/service/search_home_plan_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}


// Search Home Plan by stage Admin

function SearchHomeplanAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/service/homeplan/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Something Bad Happened")
        }

    });


}



// Home Plan Assignment
function AssignHomePlan() {
    //var checkedValues = [];
    //alert("This is Home Plan Assignment");
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/service/assign/homeplan/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);

            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }

}



// Assignment Search home plan
function SearchHomeplanAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/service/homeplan/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}


// Life Plan Search
function SearchLifeplanOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    console.log(formDATA)
    console.log(">>>>>>")
    console.log("{{ csrf_token }}")
    console.log(Domain)
    $.ajax({
        type: 'POST',
        url: Domain + '/service/search_life_plan_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}

// Search Life Plan by stage Admin

function SearchLifeplanAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/service/lifeplan/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}

// Life Plan Assignment
function AssignLifePlan() {
    //var checkedValues = [];
    // alert("This is Life Plan Assignment");
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/service/assign/lifeplan/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }

}

// Assignment Search life plan
function SearchLifeplanAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/service/lifeplan/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}




// enterprise Plan Search
function SearchEnterpriseplanOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/service/search_enterprise_plan_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}

// Search Enterprise Plan by stage Admin

function SearchEnterpriseplanAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/service/enterpriseplan/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}

// Enterprise Plan Assignment
function AssignEnterprisePlan() {
    //var checkedValues = [];
    // alert("This is Enterprise Plan Assignment");
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/service/assign/enterpriseplan/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }

}

// Assignment Search Enterprise plan
function SearchEnterpriseplanAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/service/enterpriseplan/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}


// Search wellness feed by users Admin

function SearchWellnessfeedAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {

        $.ajax({
            type: 'POST',
            url: Domain + '/news-feed/search-news/wellness/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},

            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },

            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {

    }


}


// Assignment Search Wellness Feed
function SearchWellnessfeedOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/news-feed/assign/wellness/search_wellness_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}


// Search global feed by users Admin

function SearchGlobalfeedAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {

        $.ajax({
            type: 'POST',
            url: Domain + '/news-feed/search-news/global/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},

            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },

            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {

    }


}


// Assignment Search global Feed
function SearchGlobalfeedOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/news-feed/assign/global/search_global_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}

// Search wellness feed by stage Admin

function SearchWellnessfeedAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/news-feed/search-news/wellness/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });


}

// Assignment Search global Feed
function SearchHealthfeedOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/news-feed/assign/health/search_health_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}

// Search global feed by stage Admin

function SearchGlobalfeedAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/news-feed/search-news/global/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });


}


// Search global feed by stage Admin

function SearchHealthfeedAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/news-feed/search-news/health/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });


}

// Search global feed by users Admin

function SearchHealthfeedAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {

        $.ajax({
            type: 'POST',
            url: Domain + '/news-feed/search-news/health/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},

            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },

            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {

    }


}


function SearchHomeplanAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;

    if (formDATA.q != '') {

        $.ajax({
            type: 'POST',
            url: Domain + '/service/search/homeplan/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},

            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },

            error: function (data) {
                alert(data)
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {

    }


}
function SearchLifeplanAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {

        $.ajax({
            type: 'POST',
            url: Domain + '/service/search/lifeplan/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},

            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },

            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {

    }


}


function SearchEnterpriseplanAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {

        $.ajax({
            type: 'POST',
            url: Domain + '/service/search/enterpriseplan/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},

            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },

            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {

    }


}


// Search home service plan by publisher
function SearchhomeplanByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;

    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/service/search/homeplan/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}

// Search life service plan by publisher
function SearchlifeplanByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;

    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/service/search/lifeplan/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}


// Search enterprise service plan by publisher
function SearchenterpriseplanByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/service/search/enterpriseplan/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}

// Search service plan by publisher
function SearcheserviceplanByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/service/plan-new/search/serviceplan/by/publisher-stage/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}


// Search disease by publisher
function SearchdiseaseByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/disease/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}


// Search Disease by users Admin

function SearchDiseaseAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    alert(formDATA.q)
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/disease/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}

// Search Disease by users Admin

function SearchDrugAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;

    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/drug/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}
// Search Disease by users Admin

function SearchSymptomsAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;

    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/symptoms/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}




// Search symptoms by publisher
function SearchsymptomsByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/symptoms/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}



// Search drug by publisher
function SearchdrugByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/drug/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}


function SearchGlobal(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/global/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
           alert("Please check your Internet Connection");
        }


    });
}

function SearchWellness(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/wellness/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
           alert("Please check your Internet Connection");
        }


    });
}

function SearchHealth(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/health/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
           alert("Please check your Internet Connection");
        }


    });
}

function SearchHomePlan(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/home-plan/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
           alert("Please check your Internet Connection");
        }


    });
}

function SearchLifePlan(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/life-plan/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
           alert("Please check your Internet Connection");
        }


    });
}

function SearchEnterprisePlan(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/enterprise-plan/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
           alert("Please check your Internet Connection");
        }


    });
}

// Assignment Search Bloodbank by Nishank
function SearchAmbulanceAssignnew() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/ambulance/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}



function ServiceOfferedByCategory(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/service-offered/by/category/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}

function SpecialityByCategory(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/speciality/by/category/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}

// Search User By Name by admin
function SearchUserByNameAdmin() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    formDATA.q2 = $("#utype").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/userbyname/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}

// Search User By Name by admin
function SearchLocalityByNameAdmin() {
    var formDATA = {};
    formDATA.q = $("#search").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/search/localitybyname/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}

// Search User By Name by admin
function SearchZoneLocationByNameAdmin() {
    var formDATA = {};
    formDATA.q = $("#search").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/search/zonelocationbyname/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}




//--------BRANCH----------------Filter City on selection of State--- added by NISHANK 27 NOV 2016-------------------------------------//

$('select[name=astate_id]').change(function () {
    if ($(this).val() != '') {
        var formdata = {name: $(this).val()};
        $(".Options").remove();
        $.ajax({
            type: 'POST', url: Domain + '/get_city_byname/', data: formdata, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                //alert(resData);
                resData = JSON.parse(resData);
                //alert(resData.speciality[0].id);

                if (resData.city_list.length > 0) {
                    $('select[name=acity_id]').empty();
                    $('select[name=alocality_id]').empty();

                    $('select[name=acity_id]').append($('<option>', {
                        value: '',
                        text: "--Select City--"
                    }));

                    $('select[name=alocality_id]').append($('<option>', {
                        value: '',
                        text: "--Select Location--"
                    }));
                    $('select[name=alocality_id]').trigger("chosen:updated");

                    var i;
                    for (i = 0; i < resData.city_list.length; i++) {
                        $('select[name=acity_id]').append(new Option(resData.city_list[i].name, resData.city_list[i].id));
                    }






                    $('select[name=acity_id]').trigger("chosen:updated");
                    //alert('ok');

                }
                else {
                    $('select[name=acity_id]').empty();
                    $('select[name=acity_id]').append($('<option>', {
                        value: '',
                        text: "--No City available--"
                    }));
                    $('select[name=acity_id]').trigger("chosen:updated");
                    //alert("No City available")
                }
            },
            error: function (e) {
                alert(e.resData.message);
            }

        })

    }
});


//-----------BRANCH-------------Filter Locality on selection of State--- added by NISHANK 27NOV 2016-------------------------------------//

$('select[name=acity_id]').change(function () {
    console.log($(this).val())
    console.log($(this))
    if ($(this).val() != '') {
        var formdata = {name: $(this).val()};
        $(".Options").remove();
        $.ajax({
            type: 'POST', url: Domain + '/get_location_byname/', data: formdata, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                //alert(resData);
                ajaxindicatorstop();
                //alert(resData);
                resData = JSON.parse(resData);
                //alert(resData.speciality[0].id);
                console.log(resData);

                if (resData.location_list.length > 0) {
                    $('select[name=alocality_id]').empty();
                    $('select[name=alocality_id]').append($('<option>', {
                        value: '',
                        text: "--Select Location--"
                    }));
                    var i;
                    for (i = 0; i < resData.location_list.length; i++) {
                        $('select[name=alocality_id]').append(new Option(resData.location_list[i].name, resData.location_list[i].id));
                    }
                    $('select[name=alocality_id]').trigger("chosen:updated");
                    //alert('ok');
                }
                else {
                    $('select[name=alocality_id]').empty();
                    $('select[name=alocality_id]').append($('<option>', {
                        value: '',
                        text: "--No Location available--"
                    }));
                    $('select[name=alocality_id]').trigger("chosen:updated");
                    //alert("No Location available")
                }

            },
            error: function (e) {
                alert(e.resData.message);
            }

        })

    }
});



function SearchRehab(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/rehab/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });
}





// Search lab by publisher
function SearchrehabByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/rehab/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}





// Search Rehab by users Admin

function SearchRehabAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/rehab/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}


// Assignment Search Rehab
function SearchRehabOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/rehab/assign/search_rehab_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}



// Search Rehab by stage Admin

function SearchRehabAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    alert(formDATA.q)
    $.ajax({
        type: 'POST',
        url: Domain + '/search/rehab/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}



// Rehab Assignment
function AssignRehab() {
    //var checkedValues = [];
    // alert("This is Lab Assignment");
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/assign/rehab/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }

}

// Assignment Search lab
function SearchRehabAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/rehab/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}



function SearchAmbulanceServiceByNameAdmin() {
    var formDATA = {};
    formDATA.q = $("#search").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/search/ambulance-service-by-name-admin/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}


function SearchAmbulanceTypeByNameAdmin() {
    var formDATA = {};
    formDATA.q = $("#search").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/search/ambulance-type-by-name-admin/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}



// Search Nurse_Bureau by users Admin

function SearchNurse_BureauAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/nurse_bureau/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}


// Assignment Search Rehab
function SearchNurse_BureauOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/nurse_bureau/assign/search_nurse_bureau_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}


// Search Rehab by stage Admin

function SearchNurse_BureauAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    alert(formDATA.q)
    $.ajax({
        type: 'POST',
        url: Domain + '/search/nurse_bureau/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}



// Rehab Assignment
function AssignNurse_Bureau() {
    //var checkedValues = [];
    // alert("This is Lab Assignment");
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/assign/nurse_bureau/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }

}



function SearchNurseBureau(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/nurse_bureau/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });
}

function SearchNurse_BureauAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/nurse_bureau/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}



//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

// Search Dietitian by users Admin

function SearchDietitianAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/dietitian/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}


// Assignment Search Rehab
function SearchDietitianOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/dietitian/assign/search_dietitian_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}


// Search Rehab by stage Admin

function SearchDietitianAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    alert(formDATA.q)
    $.ajax({
        type: 'POST',
        url: Domain + '/search/dietitian/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}



// Rehab Assignment
function AssignDietitian() {
    //var checkedValues = [];
    // alert("This is Lab Assignment");
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/assign/dietitian/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }

}



function SearchDietitian(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/dietitian/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });
}

function SearchDietitianAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/dietitian/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}








//-----------BRANCH-------------Filter Organisation on selection of State--- added by NISHANK 22 NOV 2016-------------------------------------//

$('select[name=locality_id]').change(function () {
    console.log($(this).val())
    console.log($(this))
    if ($(this).val() != '' && $('#diet_org').length != 0) {
        var formdata = {name: $(this).val()};
        $(".Options").remove();
        $.ajax({
            type: 'POST', url: Domain + '/get_organisatin_byname/', data: formdata, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                //alert(resData);
                ajaxindicatorstop();
                //alert(resData);
                resData = JSON.parse(resData);
                //alert(resData.speciality[0].id);
                console.log(resData);

                if (resData.organisation_list.length > 0) {
                    $('select[name=diet_org_id]').empty();
                    $('select[name=diet_org_id]').append($('<option>', {
                        value: '',
                        text: "--Select Organisation--"
                    }));
                    var i;
                    for (i = 0; i < resData.organisation_list.length; i++) {
                        $('select[name=diet_org_id]').append(new Option(resData.organisation_list[i].name, resData.organisation_list[i].id));
                    }
                    $('select[name=diet_org_id]').trigger("chosen:updated");
                    //alert('ok');
                }
                else {
                    $('select[name=diet_org_id]').empty();
                    $('select[name=diet_org_id]').append($('<option>', {
                        value: '',
                        text: "--No Organisation available--"
                    }));
                    $('select[name=diet_org_id]').trigger("chosen:updated");
                    //alert("No Organisation available")
                }

            },
            error: function (e) {
                alert(e.resData.message);
            }

        })

    }
});

// For live doctor
$('select[name=locality_id_live_doc]').change(function () {
    console.log($(this).val())
    console.log($(this))
    if ($(this).val() != '' && $('#diet_org').length != 0) {
        var formdata = {name: $(this).val()};
        $(".Options").remove();
        $.ajax({
            type: 'POST', url: Domain + '/get_org_locality_and_stg4or5/', data: formdata, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                //alert(resData);
                ajaxindicatorstop();
                //alert(resData);
                resData = JSON.parse(resData);
                //alert(resData.speciality[0].id);
                console.log(resData);

                if (resData.organisation_list.length > 0) {
                    $('select[name=diet_org_id]').empty();
                    $('select[name=diet_org_id]').append($('<option>', {
                        value: '',
                        text: "--Select Organisation--"
                    }));
                    var i;
                    for (i = 0; i < resData.organisation_list.length; i++) {
                        $('select[name=diet_org_id]').append(new Option(resData.organisation_list[i].name, resData.organisation_list[i].id));
                    }
                    $('select[name=diet_org_id]').trigger("chosen:updated");
                    //alert('ok');
                }
                else {
                    $('select[name=diet_org_id]').empty();
                    $('select[name=diet_org_id]').append($('<option>', {
                        value: '',
                        text: "--No Organisation available--"
                    }));
                    $('select[name=diet_org_id]').trigger("chosen:updated");
                    //alert("No Organisation available")
                }

            },
            error: function (e) {
                alert(e.resData.message);
            }

        })

    }
});

//

// Search lab by publisher
function SearchDietitianByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/dietitian/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}



function SearchTherapistAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/therapist/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}



function SearchTherapistOnByStageByUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/therapist/assign/search_therapist_on_stage_user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}




function SearchTherapistAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    alert(formDATA.q)
    $.ajax({
        type: 'POST',
        url: Domain + '/search/therapist/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}




function AssignTherapist() {
    //var checkedValues = [];
    // alert("This is Lab Assignment");
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/assign/therapist/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }

}



function SearchTherapist(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/therapist/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });
}

function SearchTherapistAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/therapist/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}

function SearchTherapistByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/therapist/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}


//Search Doctor Publisher
function SearchDoctorForPublisher(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$('#ser').removeAttr('selected');
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/doctor/for-publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}


//Search Hospital Publisher
function SearchOrganisationForPublisher(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$('#ser').removeAttr('selected');
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/organisation/for-publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}

//Search Hospital Publisher
function SearchPharmacyForPublisher(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$('#ser').removeAttr('selected');
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/pharmacy/for-publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}


//Search Hospital Publisher
function SearchLabForPublisher(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$('#ser').removeAttr('selected');
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/lab/for-publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}


//Search Hospital Publisher
function SearchbloodbankForPublisher(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$('#ser').removeAttr('selected');
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/bloodbank/for-publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}



//Search Doctor Publisher
function SearchTherapistForPublisher(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$('#ser').removeAttr('selected');
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/therapist/for-publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}


//Search Doctor Publisher
function SearchAmbulanceForPublisher(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$('#ser').removeAttr('selected');
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/ambulance/for-publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}

//Search Doctor Publisher
function SearchRehabForPublisher(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$('#ser').removeAttr('selected');
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/rehab/for-publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}


// Search nurse_bureau by publisher
function Searchnurse_bureauByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/nurse_bureau/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}


//Search Nurse_Bureau Publisher
function SearchNurse_BureauForPublisher(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$('#ser').removeAttr('selected');
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/nurse_bureau/for-publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}

//Search Doctor caller and reviewer
function SearchCareDoctor(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $('#ser').removeAttr('selected');
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/care/doctor/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}



// Assignment Search Blood Bank added by Nishank
function globalsearchForAllUsers() {
    var formDATA = {};
    formDATA.value = $("#search").val();
    formDATA.type = $("#type").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/global_search_for_all_users/',
        data: {formDATA: formDATA},


        success: function (data) {
            console.log(data)
            $('div.table-responsive').replaceWith(data);
        },
        // error: function (data) {
        //     alert(formDATA.type);
        //     alert(formDATA.value);
        //     alert(url);
        //     alert("Check your Internet connection");
        // }
        error: function (data) {
                alert(JSON.stringify(data));
                  console.log(JSON.stringify(data));
                //location.reload();
            }

    });
    }


function SearchGlobalFeedForPublisher(vv) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    formDATA.user_id = vv;

    $.ajax({
        type: 'POST',
        url: Domain + '/news-feed/search-news/global/by-name/publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        // error: function (data) {
        //     alert("Check your Internet connection")
        // }

    });

}

function SearchWellnessFeedForPublisher(vv) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    formDATA.user_id = vv;

    $.ajax({
        type: 'POST',
        url: Domain + '/news-feed/search-news/wellness/by-name/publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        // error: function (data) {
        //     alert("Check your Internet connection")
        // }

    });

}

function SearchHealthFeedForPublisher(vv) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    formDATA.user_id = vv;

    $.ajax({
        type: 'POST',
        url: Domain + '/news-feed/search-news/health/by-name/publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        // error: function (data) {
        //     alert("Check your Internet connection")
        // }

    });

}

function SearchDiseaseByNamePublisher(vvv) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    formDATA.user_id = vvv;

    $.ajax({
        type: 'POST',
        url: Domain + '/search/disease/by-name/publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        // error: function (data) {
        //     alert("Check your Internet connection")
        // }

    });

}


//   ************  LIVE DOCTOR SEARCH FUNCTIONS START **********
// **********************************************************

// Search Live Doctor By users
function SearchLIveDoctorAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/live-doctor/by/users/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }

}


function SearchLIveDoctorAdminOnStageUser() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/live_doctor/by-name/on-by-stage-page/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });
}

// Search By Statges
function SearchLIveDoctorAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/live-doctor/by/stages/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert('Something Bad Happened');
                location.reload();
            }

        });
    }
    else {
        alert("Please select at least one stage")
    }
}

// Assignment Search Live Doctor
function SearchLIveDoctorAssign() {
    var formDATA = {};
    formDATA.q = $("#search").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/search/live-doctor/assign/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}


// Live Doctor Assignment functionality
function LIveDoctorAssign() {
    //var checkedValues = [];
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/assign/live-doctor/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            },
            error: function(resData){
                alert("Try Again")
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }


}

//Search Live Doctor Publisher
function SearchLIveDoctorForPublisher(user_id) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    //$('#ser').removeAttr('selected');
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/live-doctor/for-publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });
}

// **********************************************************
//   ************  LIVE DOCTOR SEARCH FUNCTIONS END **********


function SearchSymptomsByNamePublisher(vvv) {
    var formDATA = {};
    formDATA.q = $("#search").val();
    formDATA.user_id = vvv;

    $.ajax({
        type: 'POST',
        url: Domain + '/search/symptom/by-name/publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        // error: function (data) {
        //     alert("Check your Internet connection")
        // }

    });

}


//************************************************************************
//***************Search Country State City Locality Master*****************
function SearchLocalitymasterByName() {
    var formDATA = {};
    formDATA.q = $("#search").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/search/localitymaster/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}

function SearchcitymasterByName() {
    var formDATA = {};
    formDATA.q = $("#search").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/search/citymaster/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}


function FilterLocalityByCity() {
     var formDATA = {};
    formDATA.q = $("#city_id").val();
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/localitybycity/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert('Something Bad Happened');
                location.reload();
            }

        });
    }
    else {
        alert("Please select at least one stage")
    }


}

function FilterCityByState() {
     var formDATA = {};
    formDATA.q = $("#state_id").val();
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/citybystate/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert('Something Bad Happened');
                location.reload();
            }

        });
    }
    else {
        alert("Please select at least one stage")
    }


}

function SearchstatemasterByName(){
    var formDATA = {};
    formDATA.q = $("#search").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/search/statemaster/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}
function SearchCategoryMasterByName(){
     var formDATA = {};
        formDATA.q = $("#search").val();
        $.ajax({
            type: 'POST',
            url: Domain + '/search/categorymaster/by-name/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            }

        });
}

function SearchSpecialityMasterByName(){
     var formDATA = {};
        formDATA.q = $("#search").val();
        $.ajax({
            type: 'POST',
            url: Domain + '/search/speciality/by-name/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            }

        });
}

function SearchFacilityByName(){
     var formDATA = {};
        formDATA.q = $("#search").val();
        $.ajax({
            type: 'POST',
            url: Domain + '/search/facility/by-name/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            }

        });
}


function SearchDiseaseByName(){
     var formDATA = {};
        formDATA.q = $("#search").val();
        $.ajax({
            type: 'POST',
            url: Domain + '/search/disease/by-name/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            }
        });
}

function SearchLabTestByName(){
     var formDATA = {};
        formDATA.q = $("#search").val();
        $.ajax({
            type: 'POST',
            url: Domain + '/search/labtest/by-name/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            }

        });
}

function SearchDiseaseMasterByName(){
     var formDATA = {};
        formDATA.q = $("#search").val();
        $.ajax({
            type: 'POST',
            url: Domain + '/search/diseasemaster/by-name/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            }

        });
}


function SearchSymptomMasterByName(){
     var formDATA = {};
        formDATA.q = $("#search").val();
        $.ajax({
            type: 'POST',
            url: Domain + '/search/symptommaster/by-name/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            }

        });
}

function ReverseToAnyUser(type)
    {
       var checkedValues = $('input:checkbox:checked').map(function () {
           return this.value;
       }).get();
       console.log(checkedValues)

       var formDATA = {};
       checkedValues = (checkedValues).toString().toLowerCase().replace('on,','');
       if(checkedValues =='' || checkedValues ==null || checkedValues ==undefined){
           alert("Please select value....");
           return false;
       }
       formDATA.checkedValues = checkedValues;
       formDATA.reviewer_name = $("#reviewer_name").val();
       formDATA.pcfreetext = $("#pcfreetext").val();
       formDATA.rcfreetext = $("#rcfreetext").val();
       formDATA.caller_name = $("#caller_name").val();

       formDATA.prfreetext = $("#prfreetext").val();
       formDATA.callername_reviewer = $("#callername_reviewer").val();
       formDATA.publishername_revi = $("#publishername_revi").val();
       formDATA.validchoices_reviewer = $("#validchoices_reviewer").val();

       formDATA.reviewerrname_caller = $("#reviewerrname_caller").val();
       formDATA.validchoices_caller = $("#validchoices_caller").val();
       formDATA.xx = $("#xx").val();
       formDATA.typ = type;

       formDATA.publishername_admin = $("#publishername_admin").val();
       formDATA.apfreetext = $("#apfreetext").val();
       formDATA.reviewerrname_admin = $("#reviewerrname_admin").val();
       formDATA.arfreetext = $("#arfreetext").val();
       formDATA.acfreetext = $("#acfreetext").val();
       formDATA.callername_admin = $("#callername_admin").val();
//       alert(formDATA)
       $.ajax({
           type:'POST',url: Domain + '/mark/reverseto/anyuser/',data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
           success: function (response_data) {

               ajaxindicatorstop();
               
                response_data = JSON.parse(response_data);
//                alert(response_data)
                if (response_data.Redirect == true) {
                    alert(response_data.Message);
                    window.location = response_data.RedirectUrl;
                }
                else {
                    alert(response_data.Message);
                }
           },

       }
        );
    }



function NotifyDoctorForArticle(id,type){

    alert()
    var formDATA = {}
    formDATA.type = type
    formDATA.id= id

    $.ajax({
        type: 'POST',url:Domain + '/notify/doctorforarticle/',data: formDATA, beforeSend: function (){
        var text = "Request is under process"
        ajaxindicatorstart(text)
        },
        success: function(response_data){
        ajaxindicatorstop()
        response_data = JSON.parse(response_data);
        if (response_data.Redirect == true){
            alert(response_data.Message);
            windows.location = response_data.RedirectUrl;

        }
        else{
        alert(response_data.Message)
        }
        }

    });
}




// Added by Ashutosh "for searching live organisation by user "
function SearchWholeLiveOrganisation() {
    var formDATA = {};
    formDATA.q = $("#livesearch").val();
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain +'/search/whole_live_organisation/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }
}
//
//function SearchOrganisationAssign() {
//    var formDATA = {};
//    formDATA.q = $("#search").val();
//    $.ajax({
//        type: 'POST',
//        url: Domain + '/search/organisation/assign/admin/',
//        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
//        success: function (data) {
//            $('div.table-responsive').replaceWith(data);
//        },
//        error: function (data) {
//            alert("Check your Internet connection")
//        }
//
//    });
//
//}

// Search User By Name by admin
function FilterLiveOrganisationAdminByUsers(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/live_organsiation/by/user/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}

function FilterLiveOrganisationAdminStage() {
    var formDATA = {};
    formDATA.q = $("#stage_data").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/live_organisation/by/stages/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }
    });
}


// Organisation Assignment
function AssignLiveOrganisation() {
    //var checkedValues = [];
    alert("This is Organisation Assignment");
    var telecaller = $("#telecaller").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();


    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/live_organisation/assign/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }

}

function SearchLiveOrganisationByStageAdmin() {
    var formDATA = {};
    formDATA.q = $("#livesearch").val();
    formDATA.q2 = $("#utype").val();
    $.ajax({
        type: 'POST',
        url: Domain + '/search/live_organisation/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }
    });
}

function SearchLiveOrganisationByPublisher(v) {
    var formDATA = {};
    formDATA.q = v;
    if (formDATA.q != '') {
        $.ajax({
            type: 'POST',
            url: Domain + '/search/live_organisation/by/publisher/',
            data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
            success: function (data) {
                $('div.table-responsive').replaceWith(data);
            },
            error: function (data) {
                alert("Something Bad happened. Please Try again");
                location.reload();
            }

        });
    }
    else {
        alert("Please Select at least one value")
    }


}

function SearchLiveOrganisation(user_id) {
    var formDATA = {};
    formDATA.q = $("#livesearch").val();
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/live_organisation/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });
}

function SearchLiveOrganisationForPublisher(user_id) {
    var formDATA = {};
    formDATA.q = $("#livesearch").val();
    //$('#ser').removeAttr('selected');
    //$("#ser").val(select);
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/search/live_organisation/for-publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }
    });
}




function SearchDoctorNewSOByNameAdmin() {
    var formDATA = {};
    formDATA.q = $("#search").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/search/DoctorNewSOByName/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}

function SearchDoctorNewSOLooserByNameAdmin() {
    var formDATA = {};
    formDATA.q = $("#search").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/search/DoctorNewSOLooserByName/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}
//
function SearchDoctorNewSPEByNameAdmin() {
    var formDATA = {};
    formDATA.q = $("#search").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/search/DoctorNewSPEByName/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        }

    });


}



function SearchLiveDoctorForSearchRank() {
    var formDATA = {};
    formDATA.country_id = $("#id_country").val();
    formDATA.state_id = $("#id_state").val();
    formDATA.city_id = $("#id_city").val();
    formDATA.locality_id = $("#locality_id").val();
    formDATA.category_id = $("#category").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/live-doctor/get-live-docs-for-search-results/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
        success: function (data) {
            ajaxindicatorstop();
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert(data)
        }

    });

}


function SearchDoctorForSearchRank() {
    var formDATA = {};
    formDATA.country_id = $("#id_country").val();
    formDATA.state_id = $("#id_state").val();
    formDATA.city_id = $("#id_city").val();
    formDATA.locality_id = $("#locality_id").val();
    formDATA.category_id = $("#category").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/doctor/get-doctors-for-search-results/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
        success: function (data) {
            ajaxindicatorstop();
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert(data)
        }

    });

}


// function UpdateLiveDoctorRank(type,data_type){
//     var checkedValues = $('input:checkbox:checked').map(function () {
//         return this.value;
//     }).get();
//
//
//     var Spon_CC_RANK_list = $('input:text[name=Spon_CC_RANK]').map(function () {
//         return this.value;
//     }).get();
//     Spon_CC_RANK_list = Spon_CC_RANK_list.filter(function(n){ return n != "" });
//
//
//     var Spon_CLC_RANK_list = $('input:text[name=Spon_CLC_RANK]').map(function () {
//         return this.value;
//     }).get();
//     Spon_CLC_RANK_list = Spon_CLC_RANK_list.filter(function(n){ return n != "" });
//
//
//     var Subs_CC_RANK_list = $('input:text[name=Subs_CC_RANK]').map(function () {
//         return this.value;
//     }).get();
//     Subs_CC_RANK_list = Subs_CC_RANK_list.filter(function(n){ return n != "" });
//
//
//     var Subs_CLC_RANK_list = $('input:text[name=Subs_CLC_RANK]').map(function () {
//         return this.value;
//     }).get();
//     Subs_CLC_RANK_list = Subs_CLC_RANK_list.filter(function(n){ return n != "" });
//
//     var Trial_CC_RANK_list = $('input:text[name=Trial_CC_RANK]').map(function () {
//         return this.value;
//     }).get();
//     Trial_CC_RANK_list = Trial_CC_RANK_list.filter(function(n){ return n != "" });
//
//
//     var Trial_CLC_RANK_list = $('input:text[name=Trial_CLC_RANK]').map(function () {
//         return this.value;
//     }).get();
//     Trial_CLC_RANK_list = Trial_CLC_RANK_list.filter(function(n){ return n != "" });
//
//     var formDATA = {};
//     checkedValues = (checkedValues).toString().toLowerCase().replace('on,','');
//     if(checkedValues =='' || checkedValues ==null || checkedValues ==undefined){
//         alert("Please select value....");
//         return false;
//     }
//     formDATA.checkedValues = checkedValues;
//     formDATA.Spon_CC_RANK_list = Spon_CC_RANK_list;
//     formDATA.Spon_CLC_RANK_list = Spon_CLC_RANK_list;
//     formDATA.Subs_CC_RANK_list = Subs_CC_RANK_list;
//     formDATA.Subs_CLC_RANK_list = Subs_CLC_RANK_list;
//     formDATA.Trial_CC_RANK_list = Trial_CC_RANK_list;
//     formDATA.Trial_CLC_RANK_list = Trial_CLC_RANK_list;
//     formDATA.type = type;
//     formDATA.data_type = data_type;
//     if (formDATA.checkedValues != '') {
//         $.ajax({
//             type: 'POST', url: Domain + '{% url 'save-live-doctor-rank' %}', data: formDATA, beforeSend: function () {
//                 var text = 'Please wait....';
//                 ajaxindicatorstart(text);
//             },
//             success: function (resData) {
//                 ajaxindicatorstop();
//                 resData = JSON.parse(resData);
//                 if (resData.Redirect == true) {
//                     alert(resData.Message);
//                     window.location = resData.RedirectUrl;
//                 }
//                 else {
//
//                     alert(resData.Message);
//                     window.location.reload(true);
//                 }
//             },
//             error: function(data){
//                 alert('Something Bad Happened');
//                 location.reload();
//             }
//         });
//     }
//     else
//     {
//         alert("Please select bloodbanks.")
//     }
//
// }

// Service Plan Assignment
function AssignServicePlan() {
    var telecaller = $("#teleuser").val();
    var stage = $("#stage").val();

    //var checkAll = $("#checkAll").val();
    var checkedValues = $('input:checkbox:checked').map(function () {
        return this.value;
    }).get();
    var formDATA = {};
    formDATA.telecaller = telecaller;
    formDATA.stage = stage;
    formDATA.checkedValues = checkedValues;
    if (formDATA.telecaller && formDATA.stage && formDATA.checkedValues != '') {
        $.ajax({
            type: 'POST', url: Domain + '/service/plan-new/assign/serviceplan/', data: formDATA, beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
            success: function (resData) {
                ajaxindicatorstop();
                resData = JSON.parse(resData);
                if (resData.Redirect == true) {
                    alert(resData.Message);
                    window.location = resData.RedirectUrl;
                }
                else {

                    alert(resData.Message);
                }
            }
        });
    }
    else {
        alert("Please select Stage,User and Doctors");
    }
}

//Search Service Plan by admin
function SearchServicePlan() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    // formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/service/plan-new/search/serviceplan/by/admin/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
           alert("Please check your Internet Connection");
        }


    });
}

//Search Service Plan by user
function SearchServicePlanUser(user_id) {
    var formDATA = {};
    formDATA.q = $("#searchuser").val();
    formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/service/plan-new/search/serviceplan/by/user/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
           alert("Please check your Internet Connection");
        }


    });
}

//Search Service Plan by publisher
function SearchServicePlanByPublisher() {
    var formDATA = {};
    formDATA.q = $("#search").val();
    // formDATA.user_id = user_id;
    $.ajax({
        type: 'POST',
        url: Domain + '/service/plan-new/search/serviceplan/by/publisher/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
           alert("Please check your Internet Connection");
        }


    });
}


function UpdateLiveDoctorOccupiedRanks() {
    var formDATA = {};
    formDATA.occupied_values_subs = $("#occupied_values_subs").val();
    formDATA.occupied_values_spons = $("#occupied_values_spons").val();
    formDATA.type = $("#type").val();
    formDATA.key = $("#key").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/occupied-ranks/update/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
        success: function (resData) {
            resData = JSON.parse(resData)
            //redData = jQuery.parseJSON(JSON.stringify(resData));
            console.log(resData)
            ajaxindicatorstop();
            if (resData.ssuccess == 'Yes'){
                alert('ssuccess ' + resData.message)
                alert('Please CLick "Get Live Doctors" Button to refresh the values')
            }
            else{
                alert('Complete / Partial Failure ' + resData.message)
                alert('Please CLick "Get Live Doctors" Button to refresh the values')
            }

            },
        error: function (data) {
            data = JSON.parse(data)
            console.log(data)
            alert(data)
        }

    });

}



function UpdateDoctorOccupiedRanks() {
    var formDATA = {};
    //formDATA.occupied_values_subs = $("#occupied_values_subs").val();
    formDATA.occupied_values_spons = $("#occupied_values_spons").val();
    formDATA.type = $("#type").val();
    formDATA.key = $("#key").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/doctor-occupied-ranks/update/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        beforeSend: function () {
                var text = 'Please wait....';
                ajaxindicatorstart(text);
            },
        success: function (resData) {
            resData = JSON.parse(resData)
            //redData = jQuery.parseJSON(JSON.stringify(resData));
            console.log(resData)
            ajaxindicatorstop();
            if (resData.ssuccess == 'Yes'){
                alert('ssuccess ' + resData.message)
                alert('Please CLick "Get Doctors" Button to refresh the values')
            }
            else{
                alert('Complete / Partial Failure ---   ' + resData.message)
                alert('Please CLick "Get Doctors" Button to refresh the values')
            }

            },
        error: function (data) {
            data = JSON.parse(data)
            console.log(data)
            alert(data)
        }

    });

}



// Assignment Search Live Doctor
function SearchDeletedSchedulesLiveDoctor() {
    var formDATA = {};
    formDATA.q = $("#search").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/search/live-doctor/deleted-schedules-with-sponsored-ranks/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}
function SearchDeletedSchedulesDoctor() {
    var formDATA = {};
    formDATA.q = $("#search").val();

    $.ajax({
        type: 'POST',
        url: Domain + '/search/doctor/deleted-schedules-with-sponsored-ranks/',
        data: {formDATA: formDATA, csrfmiddlewaretoken: '{{ csrf_token }}'},
        success: function (data) {
            $('div.table-responsive').replaceWith(data);
        },
        error: function (data) {
            alert("Check your Internet connection")
        }

    });

}