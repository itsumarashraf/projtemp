let camera_button = document.querySelector("#start-camera");
let video = document.querySelector("#video");
let start_button = document.querySelector("#start-record");
let stop_button = document.querySelector("#stop-record");
let download_link = document.querySelector("#download-video");

let camera_stream = null;
let media_recorder = null;
let blobs_recorded = [];

camera_button.addEventListener('click', async function() {
   	camera_stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true }).catch((e) => {
        Swal.fire({
              icon: 'error',
              title: 'Permission to access camera denined',
              text: e,
            })
       });
    video.muted = true;
    video.volume = 0;
	video.srcObject = camera_stream;

  reset()
});

start_button.addEventListener('click', function() {
    // set MIME type of recording as video/webm
    video.muted = true;
    video.volume = 0;
    media_recorder = new MediaRecorder(camera_stream, { mimeType: 'video/webm' });

    start()

    // event : new recorded video blob available 
    media_recorder.addEventListener('dataavailable', function(e) {
		blobs_recorded.push(e.data);
    });

    // event : recording stopped & all blobs sent
    media_recorder.addEventListener('stop', function() {
    	// create local object URL from the recorded video blobs
    	let video_local = URL.createObjectURL(new Blob(blobs_recorded, { type: 'video/webm' }));
        
        video.muted = true;
        video.volume = 0;
    	// download_link.href = video_local;
        
        
    });

    // start recording with each recorded blob having 1 second video
    media_recorder.start(1000);
});

stop_button.addEventListener('click', function() {
	media_recorder.stop(); 
    video.muted = true;
    video.volume = 0;
    // console.log(blobs_recorded)
    pause()

    let rec = new File(blobs_recorded, 'recording.webm', {type:'video/webm'});
    // console.log(rec)
    let link = $('#postlink').attr('href');
    // console.log(link)
    let umar = new FormData();
        umar.append('file', rec);
        $.ajax({  
            type: 'POST',  
            url: link,
            processData: false,
            contentType: false,
            cache: false,
            data: umar,  
            
            success: function (out) {  
                Swal.fire(
                '',
                'Video Captured and Saved Successfully',
                'success'
              )
            }  
        });
});

let hour = 0;
let minute = 0;
let second = 0;
let millisecond = 0;

let cron;
let timee;
// document.form_main.start.onclick = () => start();
// document.form_main.pause.onclick = () => pause();
// document.form_main.reset.onclick = () => reset();

function start() {
  pause();
  cron = setInterval(() => { timer(); }, 10);
  document.getElementById('timer').style.color="red";
  timee =setInterval(() => {
    $('#rec').fadeOut(500);
    $('#rec').fadeIn(500);
  }, 1000);
    
}

function pause() {
  clearInterval(cron);
  clearInterval(timee);
}

function reset() {
  hour = 0;
  minute = 0;
  second = 0;
  millisecond = 0;
  document.getElementById('hour').innerText = '00';
  document.getElementById('minute').innerText = '00';
  document.getElementById('second').innerText = '00';
  // document.getElementById('millisecond').innerText = '000';
}

function timer() {
  if ((millisecond += 10) == 1000) {
    millisecond = 0;
    second++;
  }
  if (second == 60) {
    second = 0;
    minute++;
  }
  if (minute == 60) {
    minute = 0;
    hour++;
  }
  document.getElementById('hour').innerText = returnData(hour);
  document.getElementById('minute').innerText = returnData(minute);
  document.getElementById('second').innerText = returnData(second);
  // document.getElementById('millisecond').innerText = returnData(millisecond);
}

function returnData(input) {
  return input > 10 ? input : `0${input}`
}