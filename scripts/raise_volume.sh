amixer set Master 5%+;
VOLUME_LEVEL="$(amixer get Master | awk -F'[][]' 'END{ print $2 }')";
notify-send -t 2500 "Volume" "Raised: $VOLUME_LEVEL"