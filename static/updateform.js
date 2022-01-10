$('#submit').on('click',(e)=>{
    e.preventDefault();

    var form = $('#myfrm');
    var url = form.attr('action');

    $.ajax({
        type: "POST",
        url: url,
        data: form.serialize(), // serializes the form's elements.
        success: function()
        {
            alert("data sent successfully"); // show response from the php script.
        }
        });  
})



function addbrotherr(){
    $('.bd_sample .brothers').clone().appendTo('.morebrothershere');
}

$(document).on('click','.brotherchildadd',function(){
    let clonekid=$('#brotherdetails1 #brotherkid .brotherkidwrapper').clone();
    $(this).prev().append(clonekid)
});

$(document).on('click','.removebrother',function(){
    $(this).parent().parent().parent().remove();
})

$('#brotherdetails .morebrothershere .brothers').find('.removebrotherkid:first-child').css({"display":"none"});

$(document).on('click','.removebrotherkid',function(){
    $(this).parent().parent().parent().remove();
});

//sisters
$(document).on('click','.sistermarried',function(){
    if( $(this).prop('checked')){
        $(this).parent().parent().parent().find('.sisterfamily').show()
    }else{
        $(this).parent().parent().parent().find('.sisterfamily').hide()
    }

});

$(document).on('click','.addsisterskid',function(){
    
    let kidclone = $('#sisterdetails1 #sisterkids .sisterkidwrapper').clone();
    $(this).parent().parent().find('.moresisterkids').append(kidclone)
});

$(document).on('click','.addsister',function(){
    let clonesister = $('#sisterdetails1 .sisterwrapper').clone().find("input").val("").end();
    // clonesister.find("input:checkbox").attr("id","checkbox"+i)
    // $('.addsister').parent().parent().parent().find('.moresisters').append(clonesister)
    $('.moresisters').append(clonesister)
});

function criminalismarried(){
    var html=`<div class="marriagedetails">
                    <fieldset class="border p-3">
                        <div class="form-row">
                            <div class="form-group col-md-5">
                            <label for="spouse">Spouse</label>
                            <input type="text" name="spousename" class="form-control" id="spouse">
                            </div>
                            <div class="form-group col-md-4">
                                <label for="spousedo">Daughter of</label>
                                <input type="text" name="spousefather" class="form-control" id="spousedo">
                            </div>
                            <div class="form-group col-md-3">
                                <label for="spouseoccupation">Occupation</label>
                                <input type="text" name="spouseoccupaion" class="form-control" id="spouseoccupation">
                            </div>
                        </div>
                
                        <div class="form-row">
                            <div class="form-group col-md-6">
                                <label for="spouseaddress">Address</label>
                                <input type="text" name="spouseaddress" class="form-control" id="spouseaddress">
                            </div>
                            <div class="form-group col-md-3">
                            <label for="spouseage">Age</label>
                            <input type="text" name="spouseage" class="form-control" id="spouseage">
                            </div>
                            <div class="form-group col-md-3">
                            <label for="spousephone">Phone</label>
                            <input type="phone" name="spousephone" class="form-control" id="spousephone">
                            </div>
                        </div>
                    </fieldset>

                    <fieldset class="border p-3">
                        <div class="kidwrapper row">
                            <div class="form-row">
                                <div class="form-group col-md-5">
                                    <label for="kid">Son/Daughter</label>
                                    <input type="text" name="kidname" class="form-control" id="kid">
                                </div>
                                <div class="form-group col-md-3">
                                    <label for="kidsoccupation">Occupation</label>
                                    <input type="text" name="kidoccupation" class="form-control" id="kidsoccupation">
                                </div>
                                <div class="form-group col-md-2">
                                <label for="kidsage">Age</label>
                                <input type="text" name="kidage" class="form-control" id="kidsage">
                                </div>
                                <div class="form-group col-md-2">
                                <label for="kidsphone">Phone</label>
                                <input type="phone" name="kidphone" class="form-control" id="kidsphone">
                                </div>
                            </div>
    
                            <div class="form-row">
                                <div class="form-group col-md-6">
                                <label for="kidschool">School</label>
                                <input type="text" name="kidschool" class="form-control" id="kidschool" placeholder="School.">
                                </div>
                                <div class="form-group col-md-6">
                                <label for="kidcollege">College</label>
                                <input type="text" name="kidcollage" class="form-control" id="kidcollege" placeholder="college">
                                </div>
                            </div>
                        </div>
                        <a class="btn btn-sm btn-danger float-right" onclick="addchild()"> Add Child</a>
                    </fieldset>
                </div> 
    `
   if ($('#married').prop("checked")){
    $('.marriagedetailsection').append(html);
   }else{
    $('.marriagedetails').remove();
   }
}

$(document).on('click', '.brothermarried',function(){       
    
    if ($(this).prop('checked')){
    $(this).parent().parent().find('.brothersfamily').show();
   }else{
    $(this).parent().parent().find('.brothersfamily').hide();
   }
})



    


function addchild(){
    var html =`     <div class="dfield">
                        <div class="form-row">
                            <div class="form-group col-md-5">
                                <label for="kid">Son/Daughter</label>
                                <input type="text" name="kidname" class="form-control" id="kid">
                            </div>
                            <div class="form-group col-md-3">
                                <label for="kidsoccupation">Occupation</label>
                                <input type="text" name="kidoccupation" class="form-control" id="kidsoccupation">
                            </div>
                            <div class="form-group col-md-2">
                            <label for="kidsage">Age</label>
                            <input type="text" name="kidage" class="form-control" id="kidsage">
                            </div>
                            <div class="form-group col-md-2">
                            <label for="kidsphone">Phone</label>
                            <input type="phone" name="kidphone" class="form-control" id="kidsphone">
                            </div>
                        </div>

                        <div class="form-row">
                            <div class="form-group col-md-6">
                            <label for="kidschool">School</label>
                            <input type="text" name="kidschool" class="form-control" id="kidschool" placeholder="School.">
                            </div>
                            <div class="form-group col-md-4">
                            <label for="kidcollege">College</label>
                            <input type="text" name="kidcollage" class="form-control" id="kidcollege" placeholder="college">
                            </div>
                            <div class="form-group col-md-1">
                                <label for="kidcollege"></label>
                                <a class="btn btn-sm btn-danger removekid">Remove</a>
                            </div>
                        </div>
                    </div>
    
    `
    $('.kidwrapper').append(html);
}

$(document).on('click', '.removekid', function(){
    $(this).parents('.dfield').remove(); 
});

function addvehical(){
    html= `
    <div class="form-group col-md-5">
                <label for="vehical">Vehical Owned</label>
                <input type="text" name="vehicalname" class="form-control" id="vehical">
            </div>
            <div class="form-group col-md-3">
                <label for="vehicaltype">Type</label>
                <select class="form-control" id="vehicaltype">
                <option value="car">Car</option>
                <option value="bike">Bike</option>
                <option value="other">Other</option>
                </select>
            </div>
            <div class="form-group col-md-4">
                <label for="property">Registraion No</label>
                <input type="text" name="vehicalregno" class="form-control" id="registration">
            </div>`
    $('.mobility').append(html);
}