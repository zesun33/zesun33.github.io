# Local Jekyll preview via Docker (Windows-friendly when Ruby/Bundler are not on PATH).
# Prerequisites:
#   1. Docker Desktop running
#   2. Junction: C:\zesun-site -> this repo (paths with spaces break Docker mounts)
#        New-Item -ItemType Junction -Path 'C:\zesun-site' -Target '<absolute-path-to-personal-website>'
# Usage:
#   npm run preview:docker
#   # or: powershell -NoProfile -ExecutionPolicy Bypass -File _scripts/docker-serve.ps1
# Site: http://127.0.0.1:4000/
# Stop: docker stop zesun-jekyll

docker rm -f zesun-jekyll 2>$null
docker run --rm --name zesun-jekyll `
  -v "C:/zesun-site:/srv/jekyll" `
  -p 4000:4000 `
  -p 35729:35729 `
  -e JEKYLL_ENV=development `
  jekyll/jekyll:4 `
  bash -lc "bundle install && bundle exec jekyll serve --host 0.0.0.0 --port 4000 --livereload --drafts --force_polling --config _config.yml,_scripts/preview_overrides.yml"
