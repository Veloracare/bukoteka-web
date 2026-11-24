"""Odredišne stranice po djelatnosti (SEO, 24. 11. 2026.).

Stil i podnožje preuzimaju se iz index.html (isti <style>), pa stranice prate dizajn naslovnice.
Usluge i trajanja = predlošci iz aplikacije (~/code/termino/web/app.js, `presets`), boja = TEMA_PO_DJELATNOSTI.
Tvrdnje samo o onome što aplikacija radi (vidi FAQ na naslovnici). Pokretanje iz korijena repoa:
    python3 alati/djelatnosti.py
"""
import html, json, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = (ROOT / 'index.html').read_text(encoding='utf-8')
STYLE = re.search(r'<style>.*?</style>', INDEX, re.S).group(0)

EXTRA = """<style>
.lp-hero{padding:56px 0 24px}
.lp-hero .lead{font-size:clamp(18px,2.4vw,21px);color:var(--muted);max-width:640px;margin:0 0 26px}
.lp-grid{display:grid;gap:28px;align-items:start}
@media(min-width:860px){.lp-grid{grid-template-columns:1.1fr .9fr}}
.lp-list{list-style:none;padding:0;margin:0;display:grid;gap:10px}
.lp-list li{background:var(--paper);border-radius:18px;padding:14px 18px;box-shadow:var(--sh1);display:flex;justify-content:space-between;gap:12px}
.lp-list li span{color:var(--muted);white-space:nowrap}
.lp-shot{max-width:320px;margin:0 auto}
.lp-shot img{width:100%;height:auto;border-radius:28px;box-shadow:var(--sh2)}
.lp-points{display:grid;gap:14px;margin:0;padding:0;list-style:none}
.lp-points li{background:var(--paper);border-radius:20px;padding:18px 20px;box-shadow:var(--sh1)}
.lp-points b{display:block;margin-bottom:4px}
.lp-related{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.lp-related a{background:var(--paper);border-radius:999px;padding:8px 16px;box-shadow:var(--sh1);text-decoration:none;color:var(--ink);font-weight:500}
.crumbs{font-size:14px;color:var(--muted);margin:0 0 14px}.crumbs a{color:inherit}
</style>"""

PAGES = [
  dict(slug='za-frizere', ime='Frizeri', title='Aplikacija za frizere: termini i online naručivanje · Bukoteka',
       desc='Bukoteka za frizerske salone: muško i žensko šišanje, feniranje i trajanja upisana unaprijed. Termin upisuješ dodirom, klijenti mogu i sami. 30 dana besplatno.',
       h1='Aplikacija za frizerski salon: <em>termini dodirom.</em>',
       lead='Klijentica nazove dok imaš boju u rukama? U Bukoteci dodirneš prazno mjesto, odabereš uslugu i klijenticu, i termin je upisan. Bilježnica može ostati u ladici.',
       usluge=[('Muško šišanje', 15), ('Žensko šišanje', 30), ('Feniranje', 20), ('Šišanje i feniranje', 50)], tema='koraljna',
       shot=('03-brzi-upis', 'Brzi upis termina za frizerski salon u Bukoteci (testni podaci)'),
       tocke=[('Vrijeme na minutu', 'Termin u 9:07? Početak namjestiš točno kako ste se dogovorili, bez zaokruživanja na pola sata.'),
              ('Spremljeni klijenti', 'Ime i telefon upišeš jednom. Sljedeći put klijenticu samo odabereš s popisa.'),
              ('Više frizerki, jedan pregled', 'Svaka osoba ima svoje radno vrijeme i usluge, a ti vidiš cijeli salon na jednom mjestu.')],
       faq=[('Mogu li promijeniti usluge i trajanja?', 'Da. Predložene usluge su samo početak: dodaješ, brišeš i mijenjaš usluge i njihova trajanja kako radiš u svom salonu.'),
            ('Može li klijentica odabrati frizerku?', 'Uz Bukoteku Online klijentica na poveznici bira uslugu, vrijeme i osobu kod koje želi, ili „bilo tko slobodan”. Ti potvrdiš zahtjev.'),
            ('Šalje li Bukoteka podsjetnike klijenticama?', 'Ne. Bukoteka trenutno ne šalje automatske SMS ni e-mail poruke. Nakon potvrde online rezervacije klijentica termin može dodati u svoj kalendar na mobitelu.')],
       srodne=['za-barbere', 'za-masazu']),
  dict(slug='za-barbere', ime='Barberi i brijačnice', title='Aplikacija za barbere i brijačnice: raspored termina · Bukoteka',
       desc='Raspored termina za barber shop i brijačnicu: šišanje, brada ili oboje, svaki brijač sa svojim rasporedom. Klijenti biraju termin preko poveznice. 30 dana besplatno.',
       h1='Termini za barber shop, <em>bez poruka tamo-amo.</em>',
       lead='Petak u pet je svima omiljen termin. U Bukoteci cijeli dan vidiš na jednom ekranu, a klijent preko tvoje poveznice sam vidi tko je kad slobodan.',
       usluge=[('Šišanje', 30), ('Uređivanje brade', 20), ('Šišanje i brada', 45)], tema='čelično plava',
       shot=('02-raspored-satnica', 'Dnevna satnica brijačnice u Bukoteci (testni podaci)'),
       tocke=[('Svaki brijač svoj raspored', 'Radno vrijeme, odmori i usluge za svaku osobu posebno. Klijent bira kod koga želi.'),
              ('Upis dok šišaš', 'Dodirneš prazno mjesto, odabereš uslugu i klijenta. Nekoliko dodira, bez tipkanja.'),
              ('Poveznica za Instagram', 'Uz Bukoteku Online poveznicu za rezervacije staviš u profil, a ti samo potvrđuješ zahtjeve.')],
       faq=[('Mogu li ostaviti termine samo za stalne klijente?', 'Termine upisuješ i sam, a online rezervacije uključuješ samo ako želiš (Bukoteka Online). Svaki online zahtjev potvrđuješ ili odbiješ.'),
            ('Radi li na mobitelu?', 'Da. Bukoteka radi u pregledniku na mobitelu, tabletu i računalu, bez instalacije.'),
            ('Mogu li dodati drugog brijača kasnije?', 'Da. Osobu dodaš kad god želiš, pošalješ joj poveznicu za prijavu i možeš joj ukinuti pristup kad želiš.')],
       srodne=['za-frizere', 'za-osobne-trenere']),
  dict(slug='za-vulkanizere', ime='Vulkanizeri', title='Naručivanje za vulkanizere: termini za zamjenu guma · Bukoteka',
       desc='Termini za zamjenu i balansiranje guma po satnici, bez dvostrukih upisa u sezoni. Klijent šalje zahtjev preko poveznice, ti potvrdiš. 30 dana besplatno.',
       h1='Termini za zamjenu guma, <em>bez gužve u sezoni.</em>',
       lead='Zimske gume, a svi su zvali za deset sati? U Bukoteci svaki termin ima svoje mjesto i trajanje, pa se dva auta ne upišu u isto vrijeme.',
       usluge=[('Zamjena guma', 30), ('Balansiranje kotača', 30)], tema='čelično plava',
       shot=('01-raspored', 'Raspored dana za vulkanizersku radionicu u Bukoteci (testni podaci)'),
       tocke=[('Cijeli dan na jednom ekranu', 'Vidiš što je sljedeće i gdje ima mjesta, i na mobitelu u radionici i na računalu.'),
              ('Zahtjevi preko poveznice', 'Uz Bukoteku Online klijent pošalje zahtjev za termin. Dok zahtjev čeka tvoju potvrdu, to vrijeme nitko drugi ne može uzeti.'),
              ('Radno vrijeme i blagdani', 'Pauze i slobodni dani su u rasporedu, a hrvatski blagdani su već upisani.')],
       faq=[('Mogu li dodati i druge usluge, npr. skladištenje guma?', 'Da. Usluge i njihova trajanja upisuješ sam, predlošci su samo početak.'),
            ('Moraju li klijenti otvoriti račun?', 'Ne. Klijent otvori tvoju poveznicu, odabere uslugu i vrijeme te upiše ime i telefon.'),
            ('Imam dva radnika. Može li svaki imati svoj raspored?', 'Da. Svakoj osobi upišeš radno vrijeme i usluge, a svaki termin vežeš uz osobu koja ga radi.')],
       srodne=['za-groomere', 'za-osobne-trenere']),
  dict(slug='za-groomere', ime='Grooming saloni', title='Aplikacija za groomere: termini za šišanje pasa · Bukoteka',
       desc='Bukoteka za grooming salone: šišanje malog i velikog psa s pravim trajanjem, dnevni odmor i slobodni dani u rasporedu. Rezervacije i preko poveznice.',
       h1='Grooming salon: <em>termini za male i velike pse.</em>',
       lead='Vlasnik nazove, a ti upravo kupaš psa? Bukoteka pamti tko dolazi i koliko traje, a uz Bukoteku Online vlasnik pošalje zahtjev i kad ne možeš na telefon.',
       usluge=[('Šišanje malog psa', 60), ('Šišanje velikog psa', 90)], tema='jantarna',
       shot=('11-javna-stranica-usluge', 'Javna stranica za rezervacije s odabirom usluge (testni podaci)'),
       tocke=[('Pravo trajanje za svakog psa', 'Mali i veliki pas nisu isti posao. Svaka usluga ima svoje trajanje, pa se termini ne preklapaju.'),
              ('Pauza ostaje pauza', 'Dnevni odmor i slobodni dani su u rasporedu, pa nitko ne upiše termin u vrijeme pauze.'),
              ('Vlasnici na jednom mjestu', 'Ime i telefon upišeš jednom, sljedeći put vlasnika samo odabereš.')],
       faq=[('Mogu li dodati kupanje ili rezanje noktiju?', 'Da. Usluge i trajanja upisuješ sam, predlošci su samo početak.'),
            ('Kako vlasnik rezervira termin?', 'Uz Bukoteku Online vlasnik otvori tvoju poveznicu, odabere uslugu i vrijeme. Ti potvrdiš ili odbiješ zahtjev.'),
            ('Šalje li Bukoteka podsjetnike?', 'Ne, automatske SMS ni e-mail poruke zasad ne šalje. Nakon potvrde vlasnik termin može dodati u svoj kalendar na mobitelu.')],
       srodne=['za-vulkanizere', 'za-masazu']),
  dict(slug='za-masazu', ime='Masaža i wellness', title='Raspored termina za masažu i wellness · Bukoteka',
       desc='Raspored za masažu, wellness i spa: masaža leđa ili tijela s trajanjem koje postaviš, klijent bira terapeuta ili bilo tko slobodan. 30 dana besplatno.',
       h1='Termini za masažu i wellness, <em>bez dvostrukih upisa.</em>',
       lead='Dok masiraš, ne možeš na telefon. Uz Bukoteku Online klijent preko poveznice pošalje zahtjev za termin, a ti ga potvrdiš kad stigneš.',
       usluge=[('Masaža leđa', 30), ('Masaža tijela', 60), ('Spa tretman', 60), ('Sauna', 45)], tema='kadulja (zelena)',
       shot=('12-javna-stranica-termini', 'Odabir slobodnog termina na stranici za rezervacije (testni podaci)'),
       tocke=[('Klijent bira kod koga', 'Ako vas radi više, klijent bira osobu ili „bilo tko slobodan”.'),
              ('Odmor između tretmana', 'Radno vrijeme, dnevni odmor i slobodne dane postaviš za svaku osobu.'),
              ('Na mobitelu i računalu', 'Bukoteka radi u pregledniku, bez instalacije.')],
       faq=[('Mogu li odbiti online zahtjev?', 'Da. Svaki zahtjev potvrdiš ili odbiješ. Dok čeka odluku, to vrijeme nitko drugi ne može uzeti.'),
            ('Mogu li sakriti neke usluge od online rezervacija?', 'Ograničenje „osoba ne radi uslugu” vrijedi za online rezervacije, pa klijent vidi samo ono što ta osoba radi.'),
            ('Koliko košta?', 'Bukoteka 9 € mjesečno, Bukoteka Online (s rezervacijama) 15 € mjesečno. Prvih 30 dana je besplatno, bez kartice.')],
       srodne=['za-frizere', 'za-osobne-trenere']),
  dict(slug='za-osobne-trenere', ime='Osobni treneri, joga i pilates', title='Termini za osobne trenere, jogu i pilates · Bukoteka',
       desc='Raspored treninga i individualnih satova: trajanje postaviš sam, klijent bira slobodan termin preko poveznice, a ti potvrdiš. 30 dana besplatno, bez kartice.',
       h1='Treninzi po terminima: <em>klijenti biraju slobodan sat.</em>',
       lead='Individualni treninzi, konzultacije, uvodni sat joge ili pilatesa. U Bukoteci postaviš usluge i trajanja, a klijenti vide samo ono što je stvarno slobodno.',
       usluge=[('Individualni trening', 60), ('Konzultacije', 30), ('Individualni sat (joga, pilates)', 60), ('Uvodni sat', 45)], tema='kadulja (zelena)',
       shot=('06-spremljeni-klijenti', 'Popis spremljenih klijenata u Bukoteci (testni podaci)'),
       tocke=[('Tvoj tjedan na dlanu', 'Dva tjedna rasporeda na jednom ekranu, s odmorima i slobodnim danima.'),
              ('Stalni klijenti', 'Klijente spremiš jednom. Na podržanim mobitelima možeš ih odabrati iz imenika ili uvesti .vcf datoteku.'),
              ('Poveznica u bio', 'Uz Bukoteku Online poveznicu staviš na Instagram ili Google profil, a zahtjeve potvrđuješ ti.')],
       faq=[('Mogu li voditi grupne treninge?', 'Bukoteka je napravljena za termine s jednim klijentom. Grupne satove s više prijava na isti termin zasad ne podržava.'),
            ('Radi li i za instrukcije ili fotografe?', 'Da. Ako radiš po terminima, postaviš svoje usluge i trajanja. Predlošci postoje i za instrukcije, fotografiju i savjetovanje.'),
            ('Što nakon 30 dana probe?', 'Ništa se ne naplaćuje automatski. Podatke možeš pregledati i izvesti, a za nove upise biraš pretplatu.')],
       srodne=['za-masazu', 'za-barbere']),
]
NAZIV = {p['slug']: p['ime'] for p in PAGES}
ALL = [('za-frizere', 'frizeri'), ('za-barbere', 'barberi'), ('za-vulkanizere', 'vulkanizeri'), ('za-groomere', 'groomeri'), ('za-masazu', 'masaža'), ('za-osobne-trenere', 'treneri')]


def page(p):
    url = f"https://bukoteka.hr/{p['slug']}"
    app = f"https://app.bukoteka.hr/?utm_source=web&utm_medium=odredisna&utm_campaign={p['slug']}"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Bukoteka", "item": "https://bukoteka.hr/"},
            {"@type": "ListItem", "position": 2, "name": p['ime'], "item": url}]},
        {"@type": "WebApplication", "name": "Bukoteka", "url": "https://app.bukoteka.hr/", "applicationCategory": "BusinessApplication",
         "operatingSystem": "Web", "inLanguage": "hr", "publisher": {"@id": "https://bukoteka.hr/#organization"},
         "offers": [{"@type": "Offer", "name": "Bukoteka", "price": "9.00", "priceCurrency": "EUR"},
                    {"@type": "Offer", "name": "Bukoteka Online", "price": "15.00", "priceCurrency": "EUR"}]}]}
    e = html.escape
    usl = ''.join(f'<li>{e(n)}<span>{m} min</span></li>' for n, m in p['usluge'])
    toc = ''.join(f'<li><b>{e(a)}</b>{e(b)}</li>' for a, b in p['tocke'])
    faq = ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in p['faq'])
    rel = ''.join(f'<a href="/{s}">Bukoteka za: {e(NAZIV[s].lower())}</a>' for s in p['srodne']) + '<a href="/">Naslovnica</a>'
    return f"""<!doctype html>
<html lang="hr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(p['title'])}</title>
<meta name="description" content="{e(p['desc'])}">
<meta name="theme-color" content="#eca49d">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Bukoteka">
<meta property="og:locale" content="hr_HR">
<meta property="og:title" content="{e(p['title'])}">
<meta property="og:description" content="{e(p['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://bukoteka.hr/og-image.png">
<meta name="twitter:card" content="summary_large_image">
{STYLE}
{EXTRA}
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<header class="top">
  <div class="wrap">
    <a class="brand" href="/" aria-label="Bukoteka"><img class="brandicon" src="/favicon.svg" width="34" height="34" alt=""><span>bukoteka</span></a>
    <div class="topnav"><a class="btn btn-accent btn-small" href="/#kontakt">Kontakt</a></div>
  </div>
</header>
<main>
<section class="lp-hero">
  <div class="wrap">
    <p class="crumbs"><a href="/">Bukoteka</a> › {e(p['ime'])}</p>
    <h1>{p['h1']}</h1>
    <p class="lead">{e(p['lead'])}</p>
    <div class="cta"><a class="btn btn-primary" href="{app}"><span class="plus" aria-hidden="true">+</span>Isprobaj 30 dana besplatno</a></div>
    <p class="note">Bez kartice i bez automatske naplate. Radi u pregledniku na mobitelu i računalu.</p>
  </div>
</section>
<section class="tight">
  <div class="wrap lp-grid">
    <div>
      <p class="eyebrow">Kako počinješ</p>
      <h2>Usluge su već predložene<span class="dot">.</span></h2>
      <p class="sub">Kad odabereš djelatnost, Bukoteka predloži usluge i trajanja, a sučelje dobije {e(p['tema'])} boju. Sve možeš promijeniti.</p>
      <ul class="lp-list">{usl}</ul>
    </div>
    <figure class="lp-shot"><img src="/img/app/{p['shot'][0]}.jpg" width="560" height="1214" loading="lazy" alt="{e(p['shot'][1])}"></figure>
  </div>
</section>
<section class="tight">
  <div class="wrap">
    <p class="eyebrow">Zašto Bukoteka</p>
    <h2>Što dobiješ<span class="dot">.</span></h2>
    <ul class="lp-points">{toc}</ul>
  </div>
</section>
<section class="tight">
  <div class="wrap">
    <p class="eyebrow">Cijene</p>
    <h2>Dvije ponude<span class="dot">.</span></h2>
    <ul class="lp-points">
      <li><b>Bukoteka · 9 € mjesečno ili 90 € godišnje</b>Termine upisuješ ti: raspored, usluge, radno vrijeme, odmori, klijenti i brzi upis.</li>
      <li><b>Bukoteka Online · 15 € mjesečno ili 150 € godišnje</b>Sve iz Bukoteke, uz poveznicu za rezervacije za Instagram, Facebook ili Google profil tvrtke. Zahtjeve potvrđuješ ti.</li>
    </ul>
    <p class="note">Prvih 30 dana besplatno. Cijene su konačne (Velora nije u sustavu PDV-a).</p>
  </div>
</section>
<section class="tight">
  <div class="wrap">
    <p class="eyebrow">Česta pitanja</p>
    <h2>Pitanja i odgovori<span class="dot">.</span></h2>
    <div class="faq">{faq}</div>
    <div class="lp-related">{rel}</div>
  </div>
</section>
<section class="tight">
  <div class="wrap">
    <div class="final">
      <h2>Kreni danas<span class="dot">.</span></h2>
      <p>Prvih 30 dana besplatno, ne treba ti bankovna kartica. Postavljanje traje nekoliko minuta.</p>
      <div class="cta cta-center"><a class="btn btn-primary" href="{app}"><span class="plus" aria-hidden="true">+</span>Isprobaj 30 dana besplatno</a></div>
    </div>
  </div>
</section>
</main>
<footer>
  <div class="wrap">
    <div><strong>Bukoteka</strong> je proizvod tvrtke Velora.</div>
    <div><a href="/privatnost">Zaštita privatnosti</a> · <a href="/uvjeti">Uvjeti korištenja</a> · <a href="/podrska">Podrška</a> · Stranica ne koristi kolačiće.</div>
  </div>
</footer>
</body>
</html>
"""


for p in PAGES:
    (ROOT / f"{p['slug']}.html").write_text(page(p), encoding='utf-8')
    print('ok', p['slug'], len(p['desc']))
