curl -s $1 | grep "<a href=" | cut -d '"' -f 2 | grep "http"
