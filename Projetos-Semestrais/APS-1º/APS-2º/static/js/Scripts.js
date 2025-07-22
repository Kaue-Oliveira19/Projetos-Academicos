function calcularEmissao() {
    // Captura os valores das entradas de consumo
    const carneBovina = parseFloat(document.getElementById('carneBovina').value) || 0;
    const carneSuina = parseFloat(document.getElementById('carneSuina').value) || 0;
    const frango = parseFloat(document.getElementById('frango').value) || 0;
    const peixe = parseFloat(document.getElementById('peixe').value) || 0;
    const cafe = parseFloat(document.getElementById('cafe').value) || 0;
    const ovo = parseFloat(document.getElementById('ovo').value) || 0;
    const leite = parseFloat(document.getElementById('leite').value) || 0;
    const agua = parseFloat(document.getElementById('agua').value) || 0;
    const arroz = parseFloat(document.getElementById('arroz').value) || 0;

    // Multiplica o consumo semanal
    const fatorCarneBovina = 60;
    const fatorCarneSuina = 55;
    const fatorFrango = 6;
    const fatorPeixe = 6;
    const fatorCafe = 1.9;
    const fatorOvo = 0.225;
    const fatorLeite = 0.5;
    const fatorAgua = 0.0828;
    const fatorArroz = 0.21;

    const emissaoCarneBovina = carneBovina * 1 * fatorCarneBovina;
    const emissaoCarneSuina = carneSuina * 1 * fatorCarneSuina;
    const emissaoFrango = frango * 1* fatorFrango;
    const emissaoPeixe = peixe * 1* fatorPeixe; 
    const emissaoCafe = cafe * 1* fatorCafe; 
    const emissaoOvo = ovo *1* fatorOvo; 
    const emissaoLeite = leite *1* fatorLeite;
    const emissaoAgua = agua *1* fatorAgua;
    const emissaoArroz = arroz *1* fatorArroz;

    // Soma as emissões totais
    const emissaoTotal = emissaoCarneBovina + emissaoCarneSuina + emissaoFrango + emissaoPeixe + emissaoCafe + emissaoOvo + emissaoLeite + emissaoAgua + emissaoArroz;

     // Calcula os créditos de carbono
     const limite = 50;  // Limite de 50 kg por mês
     const reducaoTotal = Math.max(0, limite - emissaoTotal);
     const creditosCarbono = reducaoTotal / 1000;  // 1 crédito = 1000 kg


    // Exibe o resultado no HTML
    document.getElementById('resultadoEmissao').textContent = emissaoTotal.toFixed(2);
    document.getElementById('creditosCarbono').textContent = `Créditos de Carbono: ${creditosCarbono.toFixed(2)}`;
}