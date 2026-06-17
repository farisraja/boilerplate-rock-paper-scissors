def player(prev_play, opponent_history=[], play_order={}):
    # Jika prev_play kosong, berarti ini adalah awal pertandingan baru. 
    # Bersihkan riwayat dan memori agar pola bot sebelumnya tidak tercampur.
    if not prev_play:
        prev_play = 'R'
        opponent_history.clear()
        play_order.clear()

    # Tambahkan langkah terakhir lawan ke dalam daftar riwayat
    opponent_history.append(prev_play)

    # Prediksi default jika kita belum memiliki cukup data
    prediction = 'P'

    # Jika sudah ada minimal 5 langkah yang terekam, mulailah menganalisis pola
    if len(opponent_history) > 4:
        # Gabungkan 5 langkah terakhir menjadi sebuah teks/string (misalnya, "RRPPS")
        last_five = "".join(opponent_history[-5:])
        
        # Simpan urutan 5 langkah ini ke dalam kamus (dictionary) dan catat jumlah kemunculannya
        play_order[last_five] = play_order.get(last_five, 0) + 1

        # Buat 3 tebakan kemungkinan untuk 5 langkah berikutnya, berdasarkan 4 langkah terakhir
        last_four = "".join(opponent_history[-4:])
        potential_plays = [
            last_four + "R",
            last_four + "P",
            last_four + "S",
        ]

        # Filter memori kita untuk hanya melihat tebakan yang memang pernah terjadi sebelumnya
        sub_order = {
            k: play_order[k]
            for k in potential_plays if k in play_order
        }

        # Jika kita pernah melihat pola-pola ini, pilih prediksi yang paling sering muncul
        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]

    # Daftar yang memetakan prediksi langkah lawan dengan langkah yang bisa mengalahkannya
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    return ideal_response[prediction]
