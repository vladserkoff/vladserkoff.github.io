TITLE = ' serkov '
CSS = 'base.css'
PAGE_FILE = 'index.html'
IMG_DIR = 'img'
VID_DIR = 'vid'

HTML_STUBS = {
    'html':
    '<html>{}</html>',
    'head':
    '<head><link rel="stylesheet" type="text/css" href="{css}"><title>{title}</title></head>',
    'img':
    '<img src="{src}" alt="{alt}">',
    'img_with_class':
    '<img class="{klass}" src="{src}" alt="{alt}">',
    'video':
    '<video autoplay loop muted poster="{poster}"><source src="{src}"></video>'
}


def make_head(css, title):
    stub = HTML_STUBS['head']
    return stub.format(css=css, title=title)


def make_row(content):
    if isinstance(content, list):
        content = ''.join(map(make_col, content))
    return '<div class="row">{}</div>'.format(content)


def make_col(content):
    if isinstance(content, list):
        content = ''.join(map(make_col, content))
    return '<div class="col">{}</div>'.format(content)


def make_img(img, klass=None):
    if klass:
        stub = HTML_STUBS['img_with_class']
        klass = ' '.join(klass)
    else:
        stub = HTML_STUBS['img']
    src = '/'.join([IMG_DIR, img])
    alt, _ = img.split('.')
    return stub.format(src=src, alt=alt, klass=klass)


def make_video(video, klass=None):
    if klass:
        stub = HTML_STUBS['video']
        klass = ' '.join(klass)
    else:
        stub = HTML_STUBS['video']
    src = '/'.join([VID_DIR, video])
    poster = _extract_poster(video)
    return stub.format(src=src, poster=poster, klass=klass)


def _extract_poster(video):
    video_name, _ = video.split('.')
    poster_name = '.'.join([video_name, 'jpg'])
    poster = '/'.join([VID_DIR, poster_name])
    return poster


def generate_site():
    head = [HTML_STUBS['head'].format(css=CSS, title=TITLE)]
    body = [
        make_img('jumpin_star.jpg'),
        [make_img('wheel.jpg'), make_img('gull.jpg')],
        make_img('rever.jpg'),
        make_img('field.jpg'),
        [make_img('forest_path.jpg'),
         make_img('donkey.jpg')],
        make_img('stairs_water.jpg'),
        make_img('suspension_bridge.jpg'),
        [make_img('tanker1.jpg'),
         make_img('tanker2.jpg')],
        [make_img('turk_ship.jpg'),
         make_img('cold.jpg')],
        [make_img('istambul_roof.jpg'),
         make_img('stone_people.jpg')],
        make_img('istambul_view.jpg'),
        make_img('ataturk.jpg'),
        [make_img('grotto.jpg'),
         make_img('palace.jpg')],
        [make_img('train_track.jpg'),
         make_img('wilams.jpg')],
        make_img('ducks.jpg'),
        make_img('karel_cemetery.jpg'),
        [make_img('karel_arch.jpg'),
         make_img('karel_cross.jpg')],
        [make_img('bunker1.jpg'),
         make_img('bunker2.jpg')],
        make_img('truck_back.jpg'),
        make_img('dprk_flag.jpg'),
        make_img('robots.jpg'),
        make_img('netto.jpg'),
        [make_img('mr-bird.jpg'),
         make_img('whynot.jpg')],
        make_img('greenvan.jpg'),
        [make_img('stains.jpg'), make_img('ball.jpg')],
        make_img('metro.jpg'),
        make_img('bikini.jpg'),
        [make_img('noshower.jpg'),
         make_img('bauhaus.jpg')],
        make_img('bumper.jpg'),
        [make_img('shand.jpg'),
         make_img('bikeshop.jpg')],
        make_img('overwatch.jpg'),
        [make_img('lights.jpg'),
         make_img('struggle.jpg')],
        [make_img('mirrors.jpg'),
         make_img('typography.jpg')],
        make_img('yalta.jpg'),
        [make_img('cupoladva.jpg'),
         make_img('cupolaraz.jpg')],
        make_img('doooors.jpg'),
        [make_img('tanzi.jpg'),
         make_img('tanzitut.jpg')],
        make_img('yaltruck.jpg'),
        [make_img('yaltaport.jpg'),
         make_img('mcdonalds.jpg')],
        make_img('tarhannames.jpg'),
        [make_img('tarhanlayers.jpg'),
         make_img('tarhanrock.jpg')],
        make_img('crying.jpg'),
        [make_img('birdie.jpg'),
         make_img('conductor.jpg')],
        make_img('bwzhig.jpg'),
        make_img('shelf.jpg'),
        make_img('tv.jpg'), [make_img('plaque.jpg'),
                             make_img('pray.jpg')],
        make_img('down.jpg'),
        make_img('us.jpg'),
        make_img('wine.jpg'),
        make_img('cafe.jpg'),
        make_img('sapporo.jpg'),
        make_img('feet.jpg'),
        make_img('flag.jpg'),
        make_img('phones.jpg'),
        make_img('heli.jpg'), [make_img('14-15.jpg'),
                               make_img('street.jpg')],
        make_img('market.jpg'),
        [
            make_img('bagsha.jpg', klass=['noborder', 'flipped']),
            make_img('bagsha.jpg', klass=['noborder'])
        ],
        make_img('bybuddha.jpg'),
        make_img('piles.jpg'),
        make_video('datsan.mp4'),
        make_img('jetstream.jpg'),
        make_video('view.mp4'),
        [
            make_img('yoga.jpg', klass=['noborder']),
            make_img('yoga.jpg', klass=['noborder', 'flipped'])
        ],
        [
            make_img('mir.jpg', klass=['noborder', 'flipped']),
            make_img('mir.jpg', klass=['noborder'])
        ],
        make_img('last.jpg'),
        make_img('pogrom.jpg'),
        [make_img('melodiya.jpg'),
         make_img('zhiguli.jpg')],
        [
            make_img('radiola.jpg', klass=['noborder']),
            make_img('radiola.jpg', klass=['noborder', 'flipped'])
        ],
        make_img('death.jpg'),
        [make_img('kotel.jpg'),
         make_img('watergun.jpg')],
        [
            make_img('rest.jpg', klass=['noborder']),
            make_img('rest.jpg', klass=['noborder', 'flipped'])
        ],
        make_img('fort.jpg'),
        make_img('beuys.jpg'),
        [
            make_img('facev.jpg', klass=['noborder']),
            make_img('facev.jpg', klass=['noborder'])
        ],
        make_img('cammo.jpg'),
        make_img('piss.jpg'),
        make_img('yard.jpg'),
        [
            make_col([
                make_img('circles.jpg', klass=['noborder', 'flipped']),
                make_img('circles.jpg', klass=['noborder'])
            ]),
            make_img('cow.jpg')
        ],
        make_img('orange.jpg'),
        make_img('noshit.jpg'),
        make_img('metrolegs.jpg'),
        [make_img('tunnel.jpg'),
         make_img('emptytruck.jpg')],
        [make_img('trolleynight.jpg'),
         make_img('hohloma.jpg')],
        make_img('wings.jpg'),
        [make_img('meteor.jpg'),
         make_img('meteorrear.jpg')],
        [make_img('shipworks.jpg'),
         make_img('boat.jpg')],
        make_img('rocks.jpg'),
        [
            make_img('stairs.jpg', klass=['noborder', 'flipped']),
            make_img('stairs.jpg', klass=['noborder'])
        ],
        make_img('peterview.jpg'),
        make_img('alley.jpg'),
        make_img('soar.jpg'),
        make_img('station.jpg'),
        [make_img('truck.jpg', klass=['flipped']),
         make_img('rider.jpg')], [make_img('meat.jpg'),
                                  make_img('pipes.jpg')]
    ]
    body = list(map(make_row, body))
    html = HTML_STUBS['html'].format(''.join(head + body))
    return html


if __name__ == '__main__':
    with open(PAGE_FILE, 'w') as file:
        file.write(generate_site())
