#!/bin/zsh

FIRST_NAME="SONER"
LAST_NAME="KRAL"

for AGE in {100000..30000000}; do

  OUTPUT=$(./AgeGuesser <<EOF
$FIRST_NAME
$LAST_NAME
$AGE
EOF
)


  if echo "$OUTPUT" | grep -q "flag"; then
    echo "Success! FLAG found with age: $AGE"
    echo "Output: $OUTPUT"
    break
  fi

  echo "Tried age $AGE - No flag found."
done
