

console.log('hello from main.js file');


// ************ API TO FETCH DATA ON ZIPCODE *******************************

function myfun(){
  var pin=document.getElementById("pin").value;
  var url = `https://api.postalpincode.in/pincode/${pin}`;
  fetch(url)
  .then(response => response.json())
  .then(data => {
              console.log("--------Tehsil--------");

                data[0].PostOffice.forEach(PostOffice => {
                  console.log(PostOffice.Name)
                  var opt = document.createElement("option");
                  opt.value=PostOffice.Name;
                  opt.text=PostOffice.Name;
                  document.getElementById("village").appendChild(opt);
                })
                console.log("---------------------");
               console.log(data[0].PostOffice[0].Country);
               console.log(data[0].PostOffice[0].State);
               console.log(data[0].PostOffice[0].Division);
               document.getElementById("district").value=data[0].PostOffice[0].Division;
              document.getElementById("country").value=data[0].PostOffice[0].Country;}
  )
  .catch((error) => console.log("invalid pincode"));
  
}

// ######################################## API CALL ENDS HERE ####################################################




// ******************************** WEBCAM PHOTO FUNCTIONALITY ********************************************

let image_data_url
  let camera_button = document.querySelector("#start-camera");
  let video = document.querySelector("#video");
  let click_button = document.querySelector("#click-photo");
  let canvas = document.querySelector("#canvas");
  let selectimage= document.querySelector("#selectimage");

  camera_button.addEventListener('click', async function() {
      let stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
      video.srcObject = stream;
      click_button.style.display="block";
      camera_button.style.display="none";
      video.style.display="block";
      selectimage.style.display="none";
  });

  click_button.addEventListener('click', function() {
      canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
      image_data_url = canvas.toDataURL('image/jpeg');
      video.style.display="none";
      canvas.style.display="block"
      kill();
      // add value to input webcaming feild to post
      document.getElementById('webcamimg').value = image_data_url;

      // data url of the image
      console.log(image_data_url);
      // $.ajax({  
      //       type: 'POST',  
      //       url: `http://127.0.0.1:8000/addcriminal`,  
      //       data: { img: image_data_url },  
            
      //       success: function (out) {  
      //           alert('Image uploaded successfully..');  
      //       }  
      //   }); 
      
  });

    // stops the navigator mediadevices
  function kill(e) {  
      var stream = video.srcObject;  
      var tracks = stream.getTracks();  

      for (var i = 0; i < tracks.length; i++) {  
          var track = tracks[i];  
          track.stop();  
      }  
      video.srcObject = null;  
    }

    // previews image after choose file option by user
  let viewimg=document.querySelector("#blah");
  function readURL(input) {
    viewimg.style.display="block";
    camera_button.style.display="none";
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

// ######################################## WEBCAM PHOTO FUNCTIONALITY ENDS HERE #####################################



// ************************************* CRIMINAL FORM VALIDATION GOES HERE*******************************

$(document).ready(function(){
  var frm = $('#myform');
  var sect = $('#sect_one');
  $("#next").on('click',()=>{
    console.log('button was clicked')
    
   frm.validate({
      rules:{
              fname:{required:true},
              lname:{required:true},
              email:{email:true},
              phone:{required:true, digits:true, maxlength:10, minlength:10}, 
              pin:{required:true},
              country:{required:true},
              address:{required:true},
              village:{required:true},
              marriage:{required:true},
              gender:{required:true},
              gender:{required:true},
              lang:{required:true},
              height:{required:true, digits:true},
              identity:{required:true},
              status:{required:true},
              userpic:{required:true},
            },
      messages:{
              fname:{required:"Please Provide First Name"},
              lname:{required:"Please Provide Last Name"},
              email:{required:"Email is required",
                    email:"Please Provide Valid Email Address"},
    
              phone:{required:"Phone number is Mandatory",
                    digits:"Please provide a valid Phone number",
                    maxlength:"Please provide valid Phone number",
                    minlength:"Please provide valid Phone number"},
              pin:{required:"This field is required"},
              country:{required:"This field is required"},
              address:{required:"This field is required"},
              village:{required:"This field is required"},
              marriage:{required:"This field is required"},
              gender:{required:"This field is required"},
              dob:{required:"This field is required"},
              height:{digits:"Enter correct height"}
                 },

                 highlight: function(element) {
                  $(element).closest('.form-group').addClass('has-error');
              },
              unhighlight: function(element) {
                  $(element).closest('.form-group').removeClass('has-error');
              },
              errorElement: 'span',
              errorClass: 'help-block',
              errorPlacement: function(error, element) {
                  if(element.parent('.input-group').length) {
                      error.insertAfter(element.parent());
                  } else {
                      error.insertAfter(element);
                  }
              }
                 
  });
  
  
  if(frm.valid()){
    console.log('form is valid')
    var idd = document.querySelector(".chalo").id;
    console.log(idd)
    if(idd !== 'next'){
    document.getElementById(idd).setAttribute('id', 'next');
  }
    
  }else{
    console.log('form is not valid')
    document.getElementById('next').setAttribute('id', 'stop');
    var idd = document.querySelector(".chalo").id;
    console.log(idd)
    
  }
  });
 });


//  ######################################### CRIMINAL FORM VALIDATION ENDS HERE#########################################





// ********************************** AJAX CALL TO POST CRIMINAL DATA ***************************************

// var dt = $('#myfrm').serialize()
$('#submit').on('click',function(){
  var form = document.getElementById('myform');
  var formdata = new FormData(form);
  // formdata.append("file", $("input[id^='selectimage']")[0].files[0]);
  $.ajax({ 
          type: 'POST',  
          url: `/addcriminal`,  
          data:  formdata,
          contentType:false,
          processData:false,  
          mimeType:'multipart/form-data',

          beforeSend:function(){
                $('#submit').value="Please wait....."
          },
          success: function (out) {
              Swal.fire(
                '',
                'Data Inserted Successfully',
                'success'
              )
          },
          error: function (error){
            Swal.fire({
              icon: 'error',
              title: 'Oops.. there was some error in saving your data',
              text: error.statusText,
            })
          },
      }); 
});

// ############################################ AJAX CALL ENDS HERE ########################################

// Data Picker Initialization
$('.datepicker').datepicker();






