var ui = {
    controls_opener: null,
    control_panel: null
};

var net = {
    get : function(url, callback){
        log("getting "+url);
        var xhr = new XMLHttpRequest();
        xhr.open('GET', url, true); 
        xhr.onreadystatechange=function(){
            if(xhr.readyState==4 && xhr.status==200){
                return callback(JSON.parse(xhr.responseText));
            }
            if(xhr.readyState==4 && xhr.status!=200){
                return callback({error:true});
            }
        }; 
        xhr.send();   
    }
};

function log(text){
    console.log(text);
}

function init_ui(){
    ui.controls_opener = document.getElementById("controls_opener");
    ui.control_panel = document.getElementById("control_panel");
    if(! /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
        add_class(ui.control_panel, "open");
    }
}

function bind_listeners(){
    ui.controls_opener.onclick = toggle_controls;
}

function load_metadata(){
    net.get("data/descriptors.json", function(data){
        log(data); 
    });   
}

function toggle_controls(){
    toggle_class(ui.control_panel, "open");
}

function toggle_class(el, name){
    if(el.className.indexOf(name) == -1){
        add_class(el, name);
    }
    else{
        remove_class(el, name);
    }
}

function add_class(el, name){
    el.className += ' '+name;   
}

function remove_class(el, name){
    var elClass = ' '+el.className+' ';
    while(elClass.indexOf(' '+name+' ') != -1)
         elClass = elClass.replace(' '+name+' ', '');
    el.className = elClass;
}


init_ui();
bind_listeners();  
