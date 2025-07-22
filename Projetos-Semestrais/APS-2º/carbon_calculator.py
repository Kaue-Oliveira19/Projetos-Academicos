def calcular_carbono_alimentar(carne_bovina, frango, peixe, carne_suina, cafe, ovos, leite, agua, arroz):
    # Cálculos de emissões de carbono para cada alimento consumido semanalmente:
    
    # Carne bovina: 60 kg de CO₂ por quilo
    carbono_carne_bovina = carne_bovina * 60
    
    # Frango: 6 kg de CO₂ por quilo
    carbono_frango = frango * 6
    
    # Peixe: 6 kg de CO₂ por quilo (mesmo valor do frango para simplificação)
    carbono_peixe = peixe * 6
    
    # Carne suína: 55 kg de CO₂ por quilo
    carbono_carne_suina = carne_suina * 55
    
    # Café: 1,9 kg de CO₂ por quilo
    carbono_cafe = cafe * 1.9
    
    # Ovos: 0,225 kg de CO₂ por ovo
    carbono_ovos = ovos * 0.225
    
    # Leite: 0,5 kg de CO₂ por litro
    carbono_leite = leite * 0.5
    
    # Água: 0,0828 kg de CO₂ por litro (82,8 g por garrafa de 500 ml)
    carbono_agua = agua * 0.0828
    
    # Arroz: 0,21 kg de CO₂ por quilo
    carbono_arroz = arroz * 0.21
    
    # Somar o total de carbono
    total_carbono = (carbono_carne_bovina + carbono_frango + carbono_peixe + carbono_carne_suina +
                     carbono_cafe + carbono_ovos + carbono_leite + carbono_agua + carbono_arroz)
    
    # Conversão para créditos de carbono (1 crédito = 1 tonelada = 1000 kg)
    limite = 50  # limite de 50 kg por mês
    reducao_total = max(0, limite - total_carbono)
    creditos_carbono = reducao_total / 1000
    
    # Retorna com os valores calculados de carbono total e crédito de carbono
    return {
        'total_carbono': total_carbono,
        'creditos_carbono': creditos_carbono
    }
