// 4. Lógica do Botão Interativo
function lancarMagia() {
    const secao = document.getElementById('ex4');
    const btn = document.getElementById('btn-magia');
    
    if (btn.innerText.includes('Lumos')) {
        secao.style.backgroundColor = '#fffacd';
        secao.style.color = '#000';
        btn.innerText = 'Desativar Nox';
        btn.style.backgroundColor = '#333';
    } else {
        secao.style.backgroundColor = 'var(--card-bg)';
        secao.style.color = 'var(--text-color)';
        btn.innerText = 'Lançar Feitiço: Lumos';
        btn.style.backgroundColor = 'var(--primary-color)';
    }
}

// 5. Lógica do Sistema de Pontuação
let xp = 0;
function alterarXP(valor) {
    xp += valor;
    if (xp < 0) xp = 0; // Não deixa o XP ficar negativo
    document.getElementById('xp-display').innerText = xp;
}

// 6. Lógica do Quiz
function calcularQuiz() {
    let pontos = 0;
    const res1 = document.querySelector('input[name="q1"]:checked');
    const res2 = document.querySelector('input[name="q2"]:checked');
    const res3 = document.querySelector('input[name="q3"]:checked');

    if (res1 && res1.value === 'certo') pontos++;
    if (res2 && res2.value === 'certo') pontos++;
    if (res3 && res3.value === 'certo') pontos++;

    const feedback = document.getElementById('resultado-quiz');
    if (pontos === 3) {
        feedback.innerText = `Você acertou ${pontos}/3! Rank S - Especialista!`;
        feedback.style.color = '#2ecc71';
    } else if (pontos > 0) {
        feedback.innerText = `Você acertou ${pontos}/3. Foi bem, mas pode melhorar!`;
        feedback.style.color = '#f1c40f';
    } else {
        feedback.innerText = `Você acertou 0/3. Fim de jogo (Game Over)!`;
        feedback.style.color = '#e74c3c';
    }
}

// 7. Lógica da Troca de Tema
function alternarTema() {
    const body = document.body;
    const btn = document.getElementById('btn-tema');
    
    body.classList.toggle('light-theme');
    
    if (body.classList.contains('light-theme')) {
        btn.innerText = 'Alternar para Tema Escuro';
    } else {
        btn.innerText = 'Alternar para Tema Claro';
    }
}

// 8. Lógica da Galeria
function mostrarDetalhes(nome, descricao) {
    const divDetalhes = document.getElementById('detalhes-galeria');
    divDetalhes.style.display = 'block';
    divDetalhes.innerHTML = `<strong>${nome}:</strong> ${descricao}`;
}