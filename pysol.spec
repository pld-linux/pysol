Summary:	PySol - a solitaire game collection
Summary(pl):	PySol - kolekcja pasjansów
Name:		pysol
Version:	4.80
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://www.oberhumer.com/opensource/pysol/download/%{name}-%{version}.tar.bz2
Source1:	http://www.oberhumer.com/opensource/pysol/download/%{name}-cardsets-4.40.tar.bz2
Source2:	http://www.oberhumer.com/opensource/pysol/download/%{name}-music-4.40.tar.bz2
Source3:	http://www.oberhumer.com/opensource/pysol/download/%{name}-sound-server-2.50.tar.bz2
Source4:	%{name}.desktop
Source5:	%{name}.png
URL:		http://www.oberhumer.com/pysol
Requires:	tkinter
Requires:	python
BuildRequires:	python-devel
BuildRequires:	SDL-devel
BuildRequires:	smpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_pythonplugindir	/usr/lib/python2.1/site-packages

%description
- currently supports more than 200 distinct solitaire games
- based upon an extensible solitaire engine
- lots of classic games like Forty Thieves, FreeCell, Klondike and
  Spider
- special games like Ganjifa, Hanafuda, Poker and Tarock type games
- very nice look and feel
- multiple cardsets and backgrounds
- background table tiles
- unlimited undo & redo
- persistent bookmarks
- load & save games
- player statistics
- hint system
- demo games
- support for user written plug-ins
- sound samples and background music
- integrated HTML help browser
- lots of documentation
- written in 100%% pure Python

%description -l pl
- zawiera ponad 200 ró¿nych typów pasjansów
- oparty na rozbudowywalnym silniku
- mnówstwo klasycznych gier, takich jak Forty Thieves, FreeCell,
  Klondike i Spider
- specjalne gry, jak Ganjifa, Hanafuda, Poker i Tarock
- ³adny wygl±d
- wiele zestawów kart i te³
- kafelkowane t³o
- nieskoñczone undo i redo
- trwa³e zak³adki
- ³adowanie i zapisywanie gier
- statystyki gracza
- system podpowiedzi
- demonstracje
- wsparcie dla wtyczek u¿ytkownika
- d¼wiêki i muzyka w tle
- zintegrowana przegl±darka pomocy w HTML-u
- mnóstwo dokumentacji
- napisane w 100%% w Python-ie

%package cardsets
Summary:	Additional cardsets for pysol
Summary(pl):	Dodatkowe zestawy kart dla pysol-a
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Requires:	%{name}

%description cardsets
Additional cardsets for pysol.

%description -l pl cardsets
Dodatkowe zestawy kart dla pysol-a.

%prep
%setup -q -a 1 -a 2 -a 3
rm -rf data/cardset-2000 data/cardset-colossus data/cardset-hard-a-port data/cardset-hexadeck data/cardset-kintengu data/cardset-tuxedo data/cardset-vienna-2k
for i in pysol-cardsets-4.40/data/* ; do mv $i data/ ; done
for i in pysol-music-4.40/data/music/* ; do mv $i data/music/ ; done

%build
cd pysol-sound-server-2.50/src
%configure
%{__make}
cd ../..

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_pythonplugindir},%{_applnkdir}/Games/Card,%{_bindir},%{_datadir},%{_mandir}/man6,%{_pixmapsdir}}

install pysol-sound-server-2.50/src/pysolsoundservermodule.so $RPM_BUILD_ROOT%{_pythonplugindir}
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
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_pythonplugindir}/*
%{_mandir}/man6/*
%dir %{_datadir}/pysol
%{_datadir}/pysol/html
%{_datadir}/pysol/images
%{_datadir}/pysol/music
%{_datadir}/pysol/plugins
%{_datadir}/pysol/sound
%{_datadir}/pysol/tiles
%{_datadir}/pysol/toolbar
%{_datadir}/pysol/pysol*
%{_datadir}/pysol/cardset-standard
%doc *.gz
%{_pixmapsdir}/*
%{_applnkdir}/Games/Card/*

%files cardsets
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-[12abcdfghjklmnoprtuvwx]*
%{_datadir}/pysol/cardset-sp*
