Summary:	PySol - a solitaire game collection
Summary(pl):	PySol - kolekcja pasjansów
Name:		pysol
Version:	4.80
Release:	4
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(es):	X11/Aplicaciones/Juegos
Group(fr):	X11/Applications/Jeux
Group(pl):	X11/Aplikacje/Gry
Group(pt):	X11/Aplicações/Jogos
Source0:	http://www.oberhumer.com/opensource/pysol/download/%{name}-%{version}.tar.bz2
Source1:	http://www.oberhumer.com/opensource/pysol/download/%{name}-cardsets-4.40.tar.bz2
Source2:	http://www.oberhumer.com/opensource/pysol/download/%{name}-music-4.40.tar.bz2
Source3:	http://www.oberhumer.com/opensource/pysol/download/%{name}-%{version}-src.tar.bz2
Source4:	%{name}.desktop
Source5:	%{name}.png
URL:		http://www.oberhumer.com/pysol
Requires:	tkinter
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
- currently supports more than 200 distinct solitaire games,
- based upon an extensible solitaire engine,
- lots of classic games like Forty Thieves, FreeCell, Klondike and
  Spider,
- special games like Ganjifa, Hanafuda, Poker and Tarock type games,
- very nice look and feel,
- multiple cardsets and backgrounds,
- background table tiles,
- unlimited undo & redo,
- persistent bookmarks,
- load & save games,
- player statistics,
- hint system,
- demo games,
- support for user written plug-ins,
- sound samples and background music,
- integrated HTML help browser,
- lots of documentation,
- written in 100%% pure Python.

%description -l pl
- zawiera ponad 200 ró¿nych typów pasjansów,
- oparty na rozbudowywalnym silniku,
- mnówstwo klasycznych gier, takich jak Forty Thieves, FreeCell,
  Klondike i Spider,
- specjalne gry, jak Ganjifa, Hanafuda, Poker i Tarock,
- ³adny wygl±d,
- wiele zestawów kart i te³,
- kafelkowane t³o,
- nieskoñczone undo i redo,
- trwa³e zak³adki,
- ³adowanie i zapisywanie gier,
- statystyki gracza,
- system podpowiedzi,
- demonstracje,
- wsparcie dla wtyczek u¿ytkownika,
- d¼wiêki i muzyka w tle,
- zintegrowana przegl±darka pomocy w HTML-u,
- mnóstwo dokumentacji,
- napisane w 100%% w Python-ie.

%package cardsets
Summary:	Additional cardsets for pysol
Summary(pl):	Dodatkowe zestawy kart dla pysol-a
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(es):	X11/Aplicaciones/Juegos
Group(fr):	X11/Applications/Jeux
Group(pl):	X11/Aplikacje/Gry
Group(pt):	X11/Aplicações/Jogos
Requires:	%{name}

%description cardsets
Additional cardsets for pysol.

%description -l pl cardsets
Dodatkowe zestawy kart dla pysol-a.

%package sounds
Summary:	Sounds for pysol
Summary(pl):	D¼wiêki dla pysol-a
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(es):	X11/Aplicaciones/Juegos
Group(fr):	X11/Applications/Jeux
Group(pl):	X11/Aplikacje/Gry
Group(pt):	X11/Aplicações/Jogos
Requires:	%{name}
Requires:	%{name}-sound-server 

%description sounds
Sounds for pysol.

%description -l pl sounds
D¼wiêki dla pysol-a.

%package music
Summary:	Background music for pysol
Summary(pl):	Muzyka dla pysol-a
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(es):	X11/Aplicaciones/Juegos
Group(fr):	X11/Applications/Jeux
Group(pl):	X11/Aplikacje/Gry
Group(pt):	X11/Aplicações/Jogos
Requires:	%{name}
Requires:	%{name}-sound-server

%description music
Background music for pysol.

%description -l pl music
Muzyka dla pysol-a.

%prep
%setup -q -a 1 -a 2 
rm -rf data/cardset-2000 data/cardset-colossus data/cardset-hard-a-port \
	data/cardset-hexadeck data/cardset-kintengu data/cardset-tuxedo \
	data/cardset-vienna-2k
rm -rf data/pysol_{15,16,20,21}.pyc
for i in pysol-cardsets-4.40/data/* ; do mv $i data/ ; done
for i in pysol-music-4.40/data/music/* ; do mv $i data/music/ ; done

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Card,%{_bindir},%{_datadir},%{_mandir}/man6,%{_pixmapsdir}}

sed s\|@pkgdatadir@\|%{_datadir}/pysol\| pysol > $RPM_BUILD_ROOT%{_bindir}/pysol
mv data $RPM_BUILD_ROOT%{_datadir}/pysol

gzip -9nf README

install pysol.6 $RPM_BUILD_ROOT%{_mandir}/man6/pysol.6
install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/Games/Card
install %{SOURCE5} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/pysol
%{_datadir}/pysol/html
%{_datadir}/pysol/images
%{_datadir}/pysol/plugins
%{_datadir}/pysol/tiles
%{_datadir}/pysol/toolbar
%{_datadir}/pysol/pysol*
%{_datadir}/pysol/cardset-standard
%{_datadir}/pysol/cardset-hard-a-port
%{_datadir}/pysol/cardset-hexadeck
%{_datadir}/pysol/cardset-kintengu
%{_datadir}/pysol/cardset-vienna-2k
%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_applnkdir}/Games/Card/*

%files cardsets
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-[12abcdfgjlmnoprtuwx]*
%{_datadir}/pysol/cardset-ham*
%{_datadir}/pysol/cardset-heg*
%{_datadir}/pysol/cardset-h[ou]*
%{_datadir}/pysol/cardset-kintengu-s*
%{_datadir}/pysol/cardset-vienna-2k-s*
%{_datadir}/pysol/cardset-vienna-t*
%{_datadir}/pysol/cardset-sp*

%files sounds
%defattr(644,root,root,755)
%{_datadir}/pysol/sound

%files music
%defattr(644,root,root,755)
%{_datadir}/pysol/music
