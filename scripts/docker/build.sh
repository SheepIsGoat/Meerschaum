#! /usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
. "$DIR"/../config.sh
cd "$PARENT"

### Experimental features must be enabled and docker buildx must be installed.
### Run setup.sh to ensure everything is set up.

./scripts/docker/update_requirements.sh

docker pull "$python_image"
for t in "${tags[@]}"; do
  [ "$latest_alias" == "$t" ] && tag_latest="-t $image:latest" || unset tag_latest
  docker build \
    --build-arg dep_group="$t" \
    -t "$image:$t" ${tag_latest:-} \
    . || exit 1
done
# docker build --squash -t "$image" . || exit 1

