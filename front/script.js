const logosSelecionados = [];

const logos = {
  'AMG': 'https://logodetimes.com/times/america-mineiro/logo-america-mineiro-256.png',
  'CAP': 'https://logodetimes.com/times/atletico-paranaense/logo-atletico-paranaense-256.png',
  'CAM': 'https://logodetimes.com/times/atletico-mineiro/logo-atletico-mineiro-256.png',
  'BAH': 'https://logodetimes.com/times/bahia/logo-bahia-256.png',
  'BOT': 'https://logodetimes.com/times/botafogo/logo-botafogo-256.png',
  'BRA': 'https://logodetimes.com/times/bragantino/logo-bragantino-256.png',
  'COR': 'https://logodetimes.com/times/corinthians/logo-corinthians-256.png',
  'CUR': 'https://logodetimes.com/times/coritiba/logo-coritiba-256.png',
  'CRU': 'https://logodetimes.com/times/cruzeiro/logo-cruzeiro-256.png',
  'CUI': 'https://logodetimes.com/times/cuiaba/logo-cuiaba-256.png',
  'FLA': 'https://logodetimes.com/times/flamengo/logo-flamengo-256.png',
  'FLU': 'https://logodetimes.com/times/fluminense/logo-fluminense-256.png',
  'FOR': 'https://logodetimes.com/times/fortaleza/logo-fortaleza-256.png',
  'GOI': 'https://logodetimes.com/times/goias/logo-goias-esporte-clube-256.png',
  'GRE': 'https://logodetimes.com/times/gremio/logo-gremio-256.png',
  'INT': 'https://logodetimes.com/times/internacional/logo-internacional-256.png',
  'PAL': 'https://logodetimes.com/times/palmeiras/logo-palmeiras-256.png',
  'SAN': 'https://logodetimes.com/times/santos/logo-santos-256.png',
  'SAO': 'https://logodetimes.com/times/sao-paulo/logo-sao-paulo-256.png',
  'VAS': 'https://logodetimes.com/times/vasco-da-gama/logo-vasco-da-gama-256.png',
};

function mostrarProbabilidades() {
  alert('Probabilidades ainda não implementadas.');
}

function getLogoUrl(teamCode) {
  return logos[teamCode] || 'url_do_logo_padrao.png';
}

const homeTeamsContainer = document.getElementById('home-teams');
const awayTeamsContainer = document.getElementById('away-teams');

Object.keys(logos).forEach((team) => {
  createLogo(homeTeamsContainer, team, awayTeamsContainer);
  createLogo(awayTeamsContainer, team, homeTeamsContainer);
});

function createLogo(container, teamCode, otherBox) {
  const logo = document.createElement('img');
  logo.src = logos[teamCode];
  logo.alt = `Logo ${teamCode}`;
  logo.classList.add('clickable');
  logo.addEventListener('click', () => selectTeam(teamCode, container, otherBox));
  container.appendChild(logo);
}

function selectTeam(teamCode, selectedBox, otherBox) {
  if (!selectedBox || !otherBox) {
    console.error('Contêineres não encontrados.');
    return;
  }

  console.log(logosSelecionados)

  const isAlreadySelected = logosSelecionados.includes(teamCode);

  if (isAlreadySelected) {
    const indexToRemove = logosSelecionados.indexOf(teamCode);

    if (indexToRemove !== -1) {
      logosSelecionados.splice(indexToRemove, 1);
    }

    const isAnyLogoSelected = logosSelecionados.length > 0;

    if (isAnyLogoSelected) {
      console.log(logosSelecionados[0])
      Array.from(selectedBox.children).forEach((logo) => {
        if (logo.alt !== `Logo ${logosSelecionados[0]}`) {
          logo.style.filter = 'grayscale(0%)';
          logo.classList.remove('disabled');
          logo.classList.add('clickable');
          logo.style.transform = 'scale(1)'
        }
      });
    } else {
      Array.from(selectedBox.children).forEach((logo) => {
        if (logo.alt !== `Logo ${teamCode}`) {
          logo.style.filter = 'grayscale(0%)';
          logo.classList.remove('disabled');
          logo.classList.add('clickable');
          logo.style.transform = 'scale(1)'
        }
      });
      Array.from(otherBox.children).forEach((logo) => {
        if (logo.alt === `Logo ${teamCode}`) {
          logo.style.filter = 'grayscale(0%)';
          logo.classList.remove('disabled');
          logo.classList.add('clickable');
          logo.style.transform = 'scale(1)'
        }
      });
    }

  } else {
    Array.from(selectedBox.children).forEach((logo) => {
      if (logo.alt !== `Logo ${teamCode}`) {
        logo.style.filter = 'grayscale(100%)';
        logo.classList.remove('clickable');
        logo.classList.add('disabled');
        logo.style.transform = 'scale(0.8)'
      }
    });

    Array.from(otherBox.children).forEach((logo) => {
      if (logo.alt == `Logo ${teamCode}`) {
        logo.style.filter = 'grayscale(100%)';
        logo.classList.remove('clickable');
        logo.classList.add('disabled');
        logo.style.transform = 'scale(0.8)'
      }
    });

    logosSelecionados.push(teamCode);
  }
  console.log(logosSelecionados)
}

document.getElementById('simulate-button').addEventListener('click', simularPartida);


function simularPartida() {
  if (logosSelecionados.length < 2) {
    alert('Selecione dois times antes de simular a partida.');
    return;
  }

  const homeTeamLogo = logosSelecionados[0];
  const awayTeamLogo = logosSelecionados[1];

  const formData = new FormData();
  formData.append('sigla_casa', homeTeamLogo);
  formData.append('sigla_fora', awayTeamLogo);

  let url = 'http://127.0.0.1:5000/partida';
  const response = fetch(url, {
    method: 'post',
    body: formData,
  })
    .then(response => response.json())
    .then(data => {
      exibirResultados(data);
    })
    .catch(error => {
      console.error('Erro ao simular a partida:', error);
    });
}

function exibirResultados(data) {
  const winnerContainer = document.getElementById('winner');
  const winnerLogo = document.getElementById('winner-logo');
  
  winnerLogo.src = logos[data.vencedor];
  winnerContainer.style.display = 'block';


  const logoCasa = document.getElementById('logoCasa');
  const logoEmpate = document.getElementById('logoEmpate');
  const logoVisitante = document.getElementById('logoVisitante');
  
  logoCasa.innerHTML = `<img class="logo-small" src="${logos[logosSelecionados[0]]}" alt="Logo Casa">`;
  logoEmpate.textContent = `empate`;
  logoVisitante.innerHTML = `<img class="logo-small" src="${logos[logosSelecionados[1]]}" alt="Logo Visitante">`;


  const probabilidadeCasa = document.getElementById('probabilidadeCasa');
  const probabilidadeEmpate = document.getElementById('probabilidadeEmpate');
  const probabilidadeVisitante = document.getElementById('probabilidadeVisitante');

  probabilidadeCasa.textContent = `${data.probabilidades[0]}%`;
  probabilidadeEmpate.textContent = `${data.probabilidades[2]}%`;
  probabilidadeVisitante.textContent = `${data.probabilidades[1]}%`;

}
