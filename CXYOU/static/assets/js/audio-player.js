"use strict";
$(function()
{
    var abc;
    var myPlaylist;
    $.ajax(
        {
            url:'http://127.0.0.1:8000/musicjs/',
            type:'get',
            dataType:'json',

        }
    )
        .done(function (data) {
            console.log(data.haha);
             abc=data.haha;
              myPlaylist=new jPlayerPlaylist(
        {jPlayer:"#jquery_jplayer_1",cssSelectorAncestor:"#jp_container_1"},
        abc,
        {swfPath:"js/plugins",supplied:"oga, mp3",wmode:"window",useStateClassSkin:true,autoBlur:false,smoothPlayBar:true,keyEnabled:true,playlistOptions:{autoPlay:false}}
        );


        })
        .fail(function () {
            console.log("error");

            }
        )

    if($('.audio-player').length)
{


    $("#jquery_jplayer_1").on(
        $.jPlayer.event.ready+' '+$.jPlayer.event.play,
        function(event){
            var current=myPlaylist.current;
            var playlist=myPlaylist.playlist;
            console.log('---------------', playlist.length);//1
            $.each(playlist,function(index,obj){
                console.log('index='+index, 'current'+current);
                if(index==current){
                    $(".jp-now-playing").html("<div class='jp-track-name'>"+obj.title+"</div> " +
        "<div class='jp-artist-name'>"+obj.artist+"</div>");
                }
            });
            $('.jp-volume-bar')
                .mousedown(function(){
                    var parentOffset=$(this).offset(),width=$(this).width();
                    $(window).mousemove(function(e){
                        var x=e.pageX-parentOffset.left,volume=x/width
                        if(volume>1){
                            $("#jquery_jplayer_1").jPlayer("volume",1);
                        }else if(volume<=0){
                            $("#jquery_jplayer_1").jPlayer("mute");
                        }else{
                            $("#jquery_jplayer_1").jPlayer("volume",volume);
                            $("#jquery_jplayer_1").jPlayer("unmute");
                        }
                    });
                    return false;
                })
                .mouseup(function(){
                    $(window).unbind("mousemove");
                });
            var timeDrag=false;
            $('.jp-play-bar').mousedown(function(e){
                timeDrag=true;
                updatebar(e.pageX);
            });
            $(document).mouseup(function(e){
                if(timeDrag){
                    timeDrag=false;
                    updatebar(e.pageX);
                }
            });
            $(document).mousemove(function(e){
                if(timeDrag){
                    updatebar(e.pageX);
                }
            });
            var updatebar=function(x){
                var progress=$('.jp-progress');
                var position=x-progress.offset().left;
                var percentage=100*position/progress.width();
                if(percentage>100){percentage=100;}
                if(percentage<0){percentage=0;}
                $("#jquery_jplayer_1").jPlayer("playHead",percentage);
                $('.jp-play-bar').css('width',percentage+'%');
            };
            $('#playlist-toggle, #playlist-text, #playlist-wrap li a')
                .unbind().on('click',function(){
                    $('#playlist-wrap').fadeToggle();
                    $('#playlist-toggle, #playlist-text').toggleClass('playlist-is-visible');
                });
            $('.hide_player').unbind().on('click',function(){
                $('.audio-player').toggleClass('is_hidden');
                $(this).html($(this).html()=='<i class="fa fa-angle-down"></i> HIDE'?'<i class="fa fa-angle-up"></i> SHOW PLAYER':'<i class="fa fa-angle-down"></i> HIDE');
            });
            $('body').unbind().on('click','.audio-play-btn',function(){
                $('.audio-play-btn').removeClass('is_playing');
                $(this).addClass('is_playing');
                var playlistId=$(this).data('playlist-id');
                myPlaylist.play(playlistId);
            });
        });
}});