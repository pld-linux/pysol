Summary:	PySol - a solitaire game collection
Summary(pl):	PySol - kolekcja pasjansów
Name:		pysol
Version:	4.81
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://pysol2.sourceforge.net/download/%{name}-%{version}.tar.bz2
# Source0-md5:	3a4148f8cd4afd907f7f6798e4ab976f
Source1:	http://pysol2.sourceforge.net/download/%{name}-cardsets-4.40.tar.bz2
# Source1-md5:	cdf3749865b2f3b9d60950a9fb87185a
Source2:	http://pysol2.sourceforge.net/download/%{name}-music-4.40.tar.bz2
# Source2-md5:	08717045ef86825a1e59d5f66c3bf720
Source3:	http://pysol2.sourceforge.net/download/%{name}-%{version}-src.tar.bz2
# Source3-md5:	d7a0f5981d575da13fa444c505c75a96
Source4:	%{name}.desktop
Source5:	%{name}.png
URL:		http://www.oberhumer.com/pysol/
Requires:	python
Requires:	tkinter
Conflicts:	pysol-sound-server < 3.00
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package cardsets-classic_look
Summary:	Additional cardsets for pysol
Summary(pl):	Dodatkowe zestawy kart dla pysol-a
Group:		X11/Applications/Games
Requires:	%{name}

%description cardsets-classic_look
Additional cardsets (Classic look) for pysol.

%description cardsets-classic_look -l pl
Dodatkowe zestawy kart (Klasyczny wygl±d) dla pysol-a.

%package cardsets-collectors-1-D
Summary:	Additional cardsets for pysol
Summary(pl):	Dodatkowe zestawy kart dla pysol-a
Group:		X11/Applications/Games
Requires:	%{name}

%description cardsets-collectors-1-D
Additional cardsets (Collectors 1-D) for pysol.

%description cardsets-collectors-1-D -l pl
Dodatkowe zestawy kart (Kolekcjonerskie 1-D) dla pysol-a.

%package cardsets-collectors-F-J
Summary:	Additional cardsets for pysol
Summary(pl):	Dodatkowe zestawy kart dla pysol-a
Group:		X11/Applications/Games
Requires:	%{name}

%description cardsets-collectors-F-J
Additional cardsets (Collectors F-J) for pysol.

%description cardsets-collectors-F-J -l pl
Dodatkowe zestawy kart (Kolekcjonerskie F-J) dla pysol-a.

%package cardsets-collectors-L-N
Summary:	Additional cardsets for pysol
Summary(pl):	Dodatkowe zestawy kart dla pysol-a
Group:		X11/Applications/Games
Requires:	%{name}

%description cardsets-collectors-L-N
Additional cardsets (Collectors L-N) for pysol.

%description cardsets-collectors-L-N -l pl
Dodatkowe zestawy kart (Kolekcjonerskie L-N) dla pysol-a.

%package cardsets-collectors-P-W
Summary:	Additional cardsets for pysol
Summary(pl):	Dodatkowe zestawy kart dla pysol-a
Group:		X11/Applications/Games
Requires:	%{name}

%description cardsets-collectors-P-W
Additional cardsets (Collectors P-W) for pysol.

%description cardsets-collectors-P-W -l pl
Dodatkowe zestawy kart (Kolekcjonerskie P-W) dla pysol-a.

%package cardsets-fantasy
Summary:	Additional cardsets for pysol
Summary(pl):	Dodatkowe zestawy kart dla pysol-a
Group:		X11/Applications/Games
Requires:	%{name}

%description cardsets-fantasy
Additional cardsets (Fantasy) for pysol.

%description cardsets-fantasy -l pl
Dodatkowe zestawy kart (Fantastyczne) dla pysol-a.

%package cardsets-os
Summary:	Additional cardsets for pysol
Summary(pl):	Dodatkowe zestawy kart dla pysol-a
Group:		X11/Applications/Games
Requires:	%{name}

%description cardsets-os
Additional cardsets (Operating Systems) for pysol.

%description cardsets-os -l pl
Dodatkowe zestawy kart (Systemy operacyjne) dla pysol-a.

%package cardsets-round
Summary:	Additional cardsets for pysol
Summary(pl):	Dodatkowe zestawy kart dla pysol-a
Group:		X11/Applications/Games
Requires:	%{name}

%description cardsets-round
Additional cardsets (Round cardsets) for pysol.

%description cardsets-round -l pl
Dodatkowe zestawy kart (Kr±g³e karty) dla pysol-a.

%package cardsets-uncategorized
Summary:	Additional cardsets for pysol
Summary(pl):	Dodatkowe zestawy kart dla pysol-a
Group:		X11/Applications/Games
Requires:	%{name}

%description cardsets-uncategorized
Additional cardsets (Uncategorized) for pysol.

%description cardsets-uncategorized -l pl
Dodatkowe zestawy kart (Nieskatalogowane) dla pysol-a.

%package sounds
Summary:	Sounds for pysol
Summary(pl):	D¼wiêki dla pysol-a
Group:		X11/Applications/Games
Requires:	%{name}
Requires:	%{name}-sound-server >= 3.00

%description sounds
Sounds for pysol.

%description sounds -l pl
D¼wiêki dla pysol-a.

%package music
Summary:	Background music for pysol
Summary(pl):	Muzyka dla pysol-a
Group:		X11/Applications/Games
Requires:	%{name}
Requires:	%{name}-sound-server >= 3.00

%description music
Background music for pysol.

%description music -l pl
Muzyka dla pysol-a.

%prep
%setup -q -a 1 -a 2
rm -rf data/cardset-2000 data/cardset-colossus data/cardset-hard-a-port \
	data/cardset-hexadeck data/cardset-kintengu data/cardset-tuxedo \
	data/cardset-vienna-2k
rm -rf data/pysol_{15,16,20,21}.pyc
for i in pysol-cardsets-4.40/data/*; do
	mv $i data/;
done
for i in pysol-music-4.40/data/music/*; do
	mv $i data/music/;
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Card,%{_bindir},%{_datadir}} \
	$RPM_BUILD_ROOT{%{_mandir}/man6,%{_pixmapsdir}}

sed s\|@pkgdatadir@\|%{_datadir}/pysol\| pysol > $RPM_BUILD_ROOT%{_bindir}/pysol
mv data $RPM_BUILD_ROOT%{_datadir}/pysol

install pysol.6 $RPM_BUILD_ROOT%{_mandir}/man6/pysol.6
install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/Games/Card
install %{SOURCE5} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
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
%{_datadir}/pysol/cardset-kintengu*
%{_datadir}/pysol/cardset-vienna-2k
%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_applnkdir}/Games/Card/*

%files cardsets-classic_look
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-2000
%{_datadir}/pysol/cardset-briscola
%{_datadir}/pysol/cardset-xskat*

%files cardsets-collectors-1-D
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-1*
%{_datadir}/pysol/cardset-culemann*
%{_datadir}/pysol/cardset-denizens
%{_datadir}/pysol/cardset-dondorf*

%files cardsets-collectors-F-J
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-fantasy
%{_datadir}/pysol/cardset-gortz*
%{_datadir}/pysol/cardset-hamburg*
%{_datadir}/pysol/cardset-hegewald*
%{_datadir}/pysol/cardset-houbigant
%{_datadir}/pysol/cardset-hungarian*
%{_datadir}/pysol/cardset-joan-darc

%files cardsets-collectors-L-N
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-revolution*
%{_datadir}/pysol/cardset-liege
%{_datadir}/pysol/cardset-little*
%{_datadir}/pysol/cardset-maritimes
%{_datadir}/pysol/cardset-melange
%{_datadir}/pysol/cardset-migeon*
%{_datadir}/pysol/cardset-nickel*

%files cardsets-collectors-P-W
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-prince*
%{_datadir}/pysol/cardset-spin*
%{_datadir}/pysol/cardset-tensho
%{_datadir}/pysol/cardset-transformation
%{_datadir}/pysol/cardset-traugott*
%{_datadir}/pysol/cardset-ukiyoe-*
%{_datadir}/pysol/cardset-vienna-2k-small
%{_datadir}/pysol/cardset-vienna-tarock
%{_datadir}/pysol/cardset-wilhelmtell

%files cardsets-fantasy
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-rivers*

%files cardsets-os
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-penguins
%{_datadir}/pysol/cardset-spaced
%{_datadir}/pysol/cardset-tuxedo
%{_datadir}/pysol/cardset-xpat2

%files cardsets-round
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-mughal*
%{_datadir}/pysol/cardset-dashavatara*
%{_datadir}/pysol/cardset-get-a-round
%{_datadir}/pysol/cardset-ovale*

%files cardsets-uncategorized
%defattr(644,root,root,755)
%{_datadir}/pysol/cardset-aisleriot
%{_datadir}/pysol/cardset-colossus
%{_datadir}/pysol/cardset-gdkcard-bonded
%{_datadir}/pysol/cardset-gpl
%{_datadir}/pysol/cardset-jacoby
%{_datadir}/pysol/cardset-kabale
%{_datadir}/pysol/cardset-naylor
%{_datadir}/pysol/cardset-oxymoron*
%{_datadir}/pysol/cardset-rangoon*
%{_datadir}/pysol/cardset-spider
%{_datadir}/pysol/cardset-tksol
%{_datadir}/pysol/cardset-xpat2-*

%files sounds
%defattr(644,root,root,755)
%{_datadir}/pysol/sound

%files music
%defattr(644,root,root,755)
%{_datadir}/pysol/music
