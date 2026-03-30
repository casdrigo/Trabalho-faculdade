def jogo_adivinha_ave():
    print("="*40)
    print("🎮 BEM-VINDO AO JOGO: ADIVINHE A AVE 🎮")
    print("="*40)
    print("Pense em uma das aves da imagem (A até P).")
    print("Responda com 's' (sim) ou 'n' (não).\n")

    # PERGUNTA 1 (Divide de 16 para 8)
    p1 = input("1. O bico da ave é longo (visivelmente maior que a própria cabeça)? (s/n): ").strip().lower()

    if p1 == 's':
        # --- GRUPO: BICO LONGO (C, D, G, H, I, J, M, N) ---
        
        # PERGUNTA 2 (Divide de 8 para 4)
        p2 = input("2. A cor preta cria contraste? (s/n): ").strip().lower()
        
        if p2 == 's':
            # --- (C, D, G, M) ---
            p3 = input("3. O bico é reto? (s/n): ").strip().lower()
            
            if p3 == 's':
                # Restam: C, M
                p4 = input("4. O olho é preto?? (s/n): ").strip().lower()
                resultado = "C" if p4 == 's' else "M"
            else:
                # Restam: D, G
                p4 = input("4. O bico curva para baixo? (s/n): ").strip().lower()
                resultado = "G" if p4 == 's' else "D"
                
        else:
            # --- (C, J, M, N) ---
            p3 = input("3. O bico tem no maximo duas cores? (s/n): ").strip().lower()
            
            if p3 == 's':
                # Restam: I, N
                p4 = input("4. Tem um uma cor dominante? (s/n): ").strip().lower()
                resultado = "I" if p4 == 's' else "N"
            else:
                # Restam: H, J
                p4 = input("4. Tem uma cor dominante? (s/n): ").strip().lower()
                resultado = "H" if p4 == 's' else "J"

    else:
        # --- GRUPO: BICO CURTO/MÉDIO (A, B, E, F, K, L, O, P) ---
        
        # PERGUNTA 2 (Divide de 8 para 4)
        p2 = input("2. Em proporção a cabeça, é um bico pequeno? (s/n): ").strip().lower()
        
        if p2 == 's':
            # --- GRUPO: BICO CURTO(B, E, F, P) ---
            p3 = input("3. Sua cabeça tem mais que três cores? (s/n): ").strip().lower()
            
            if p3 == 's':
                # Restam: F, P
                p4 = input("4. A ave é careca ou tem cabeça lisa? (s/n): ").strip().lower()
                resultado = "F" if p4 == 's' else "P"
            else:
                # Restam: A, B
                p4 = input("4. A cabeça da ave tem uma divisão clara de cores? (s/n): ").strip().lower()
                resultado = "E" if p4 == 's' else "B"
                
        else:
            # --- GRUPO: BICO MÉDIO (A, K, L, O) ---
            p3 = input("3. A estrutura do bico possui duas ou mais cores? (s/n): ").strip().lower()
            
            if p3 == 's':
                # Restam: L, O
                p4 = input("4. A cabeça da ave é 'careca'? (s/n): ").strip().lower()
                resultado = "O" if p4 == 's' else "L"
            else:
                # Restam: K, A
                p4 = input("4. A base do pescoço/peito é branca? (s/n): ").strip().lower()
                resultado = "K" if p4 == 's' else "A"

    # RESULTADO FINAL
    print("\n" + "-"*40)
    print(f"🎯 A ave que você escolheu é a letra: {resultado}!")
    print("-"*40)
    #input solto só para o programa não fechar de imediato após a conclusão do jogo :)
    input()


if __name__ == "__main__":
    jogo_adivinha_ave()