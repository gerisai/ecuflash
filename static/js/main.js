const tRadio = document.getElementById('tableRadio')
const aRadio = document.getElementById('albumRadio')
const table = document.getElementById('table')
const album = document.getElementById('album')

tRadio.onchange = () => {
    table.style.display = 'table'
    album.style.display = 'none'
}

aRadio.onchange = () => {
    table.style.display = 'none'
    album.style.display = 'block'
}