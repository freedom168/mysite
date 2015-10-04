/**
 * Created by passerby on 2015/10/4.
 */
$(window).load(function() {
  $(".mdl-button").click(function() {
    $(".mdl-button").addClass("unclick-background");
    $(this).removeClass("unclick-background");
    $(this).addClass("click-background");
  });
  //$(".mdl-button").mouseenter(function() {
  //  $(this).css("background","rgba(0,0,0,0.05)");
  //});
  //$(".mdl-button").mouseleave(function() {
  //  $(this).css("background","rgba(0,0,0,0)");
  //});
  $(".apply-button").click(function() {
    $(".mdl-layout__header").css("background","rgb(66,133,244)");
  });
  $(".state-button").click(function() {
    $(".mdl-layout__header").css("background","rgb(236,164,3)");
  });
  $(".history-button").click(function() {
    $(".mdl-layout__header").css("background","rgb(15,157,88)");
  });
});

