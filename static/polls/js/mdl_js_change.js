/**
 * Created by passerby on 2015/10/3.
 */
function removeObfuscator() {
  $(window).load(function() {
    $(".mdl-layout__drawer-button").click();
    $(".mdl-layout__obfuscator").remove();
  });
}
removeObfuscator();