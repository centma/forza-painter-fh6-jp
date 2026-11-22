"""Japanese UI strings (merged into i18n.TEXT["ja"])."""

from __future__ import annotations

from version import app_title


TEXT_JA = {
    "title": app_title(),
    "subtitle": "ジオメトリ JSON を生成し、Forza Horizon のバイナルエディターへインポートします。",
    "language": "言語",
    "process": "ゲームプロセス",
    "refresh": "更新",
    "generate_tab": "JSON 生成",
    "import_tab": "インポート",
    "export_tab": "エクスポート",
    "tools_tab": "FH6 ツール",
    "tutorial_tab": "チュートリアル",
    "market_banner": "プリセットマーケット公開中: painter6.com で共有画像・プリセット・JSON パッケージを閲覧できます。",
    "open_market": "マーケットを開く",
    "images": "画像",
    "add_images": "画像を追加",
    "remove_image": "選択した画像を削除",
    "quality": "品質プロファイル",
    "gpu_device": "グラフィックカード",
    "gpu_device_auto": "自動 (最適な GPU)",
    "gpu_device_refresh": "GPU を再検出",
    "gpu_device_hint": "ジェネレーターを実行する GPU を選択します。自動の場合はジェネレーターが選択します。",
    "gpu_device_none": "OpenCL GPU が検出されません。ジェネレーターがデバイスを自動選択します。カードが表示されない場合は NVIDIA/AMD/Intel のドライバーを更新してください。",
    "gpu_device_forced": "ジェネレーター GPU: {device}",
    "gpu_device_auto_log": "ジェネレーター GPU: 自動 (ジェネレーターがデバイスを選択)。",
    "gpu_device_unsupported": "{device} はこのアプリから指定できません ({vendor} はデバイス選択に非対応)。ジェネレーターがデバイスを自動選択します。",
    "gpu_device_missing": "以前選択した GPU が見つかりません。自動に戻しました。",
    "parallel_jobs": "並列処理する画像数",
    "parallel_jobs_hint": "複数画像をキューに入れた場合のみ有効です。画像 1 枚では変わりません。",
    "parallel_jobs_active": "{jobs} 枚を同時実行中 (キュー {images} 枚)。並列実行中はレイヤー単位の残り時間を表示しません。",
    "parallel_jobs_progress": "{done}/{total} 枚完了",
    "parallel_jobs_selected": "並列生成: 最大 {jobs} 枚を同時実行。",
    "parallel_jobs_off": "並列生成オフ: 1 枚ずつ実行。",
    "parallel_jobs_incomplete": "結果が得られたのは {total} 枚中 {done} 枚のみです。実行失敗として扱います。詳細ログを確認してください。",
    "import_preset": "プリセットを読み込む",
    "open_preset_folder": "プリセットフォルダーを開く",
    "custom_settings": "カスタム設定を使用",
    "custom_layers": "出力レイヤー数",
    "custom_resolution": "最大解像度",
    "custom_random": "ランダムサンプル数",
    "custom_mutated": "変異サンプル数",
    "custom_save_at": "チェックポイント保存",
    "preprocess_mode": "前処理モード",
    "save_custom_preset": "プリセットとして保存",
    "custom_panel_title": "カスタム設定",
    "custom_panel_hint": "選択したプリセットの値が入力されます。生成前に編集する場合はカスタム設定を有効にしてください。",
    "generate_step_image": "ステップ 1 - 画像を選択",
    "generate_step_image_hint": "PNG/JPG/BMP 画像を追加します。JSON はアプリと同じ場所の out/<画像名>/<拡張子>/ に保存され、元画像は image/<拡張子>/ にバックアップされます。",
    "generate_step_quality": "ステップ 2 - 品質を選択",
    "generate_step_quality_hint": "高速プロファイルは短時間で完了します。低速プロファイルは GPU 時間を多く使い、通常はよりきれいに仕上がります。",
    "generate_step_run": "ステップ 3 - 生成",
    "generate_step_run_hint": "1 回クリックして待ちます。進捗はログに表示され、生成した JSON は自動でインポートページに追加されます。",
    "scroll_hint": "画像を追加してプリセットを選び、必要ならカスタム設定を調整します。",
    "start_generate": "現在の設定で生成",
    "stop_generate": "生成を停止",
    "open_output": "出力フォルダーを開く",
    "generate_backup_saved": "元画像を {path} にコピーしました",
    "generate_output_folder": "この画像の JSON はすべて {path} に保存されます",
    "generate_backup_failed": "元画像をバックアップできませんでした: {error}",
    "preview": "プレビュー",
    "preview_hint": "画像または JSON を選択するとここにプレビューを表示します。",
    "preview_unavailable": "プレビューを利用できません。オプションのプレビュー依存関係をインストールするか、プレビューなしで続行してください。",
    "preview_accuracy_note": "現行ビルドはゲーム内インポート精度のため楕円サイズを浮動小数で保持します。プレビューは近似です。",
    "logs": "ログ",
    "export_logs": "詳細ログをエクスポート",
    "progress": "進捗",
    "json_files": "ジオメトリ JSON ファイル",
    "add_json": "JSON を追加",
    "remove_json": "選択した JSON を削除",
    "use_outputs": "生成した JSON を使用",
    "step_game": "ステップ 1 - ゲーム",
    "step_game_hint": "FH6 を起動してバイナルグループエディターを開き、グループ解除した球体テンプレートを読み込んでからプロセス一覧を更新します。",
    "step_template": "ステップ 2 - テンプレート",
    "step_template_hint": "現在のゲーム内テンプレートに表示されている正確なレイヤー数を入力します。",
    "step_json": "ステップ 3 - JSON",
    "step_json_hint": "このアプリで生成した JSON を使うか、ジオメトリ JSON を手動で追加します。完成した最終 JSON は自動で選択されます。途中のチェックポイント JSON をインポートする場合は「JSON を追加」を使ってください。",
    "step_import": "ステップ 4 - インポート",
    "step_import_hint": "インポートを 1 回クリックします。アプリが FH6 のレイヤーテーブルを安全に検出してからデザインを書き込みます。",
    "advanced_options": "詳細オプション",
    "show_advanced": "詳細を表示",
    "hide_advanced": "詳細を隠す",
    "import_preview": "選択した JSON のプレビュー",
    "game_profile": "ゲームプロファイル",
    "pid": "PID",
    "layer_count": "テンプレートのレイヤー数",
    "easy_import": "かんたんインポート",
    "easy_import_hint": "FH6 ではアドレスは空欄のままにします。インポート前にアプリが既存セッションを再利用するか自動検出します。",
    "manual_count": "レイヤー数アドレス",
    "manual_table": "レイヤーテーブルアドレス",
    "auto_locate": "FH6 を自動検出",
    "import_json": "JSON をインポート",
    "diagnose": "診断",
    "save_snapshot": "レイヤー数スナップショットを保存",
    "compare_snapshot": "スナップショットと比較",
    "snapshot_count": "スナップショットのレイヤー数",
    "current_count": "現在のレイヤー数",
    "inspect_table": "テーブルを調査",
    "table_address": "候補テーブル",
    "admin_note": "インポートには管理者権限が必要です。OpenProcess が失敗する場合はアプリを管理者として実行してください。",
    "no_game": "対応するゲームプロセスが見つかりません",
    "layer_count_required": "テンプレートのレイヤー数は必須です。ゲーム内に表示されている正確なレイヤー数を入力してください。",
    "ready": "準備完了",
    "running": "実行中",
    "done": "完了",
    "failed": "失敗",
    "stopped": "停止",
    "no_generation_running": "実行中の生成はありません。",
    "stopping_generation": "生成を停止しています...",
    "generation_stopped": "生成を停止しました。",
    "generator_recycled_layers": "{max_layer}/{total} の時点で完全に覆われたレイヤーを再利用しました。処理を続行します。これは正常な動作で、最初からやり直しではありません。",
    "existing_final_json_found": "{image} の既存の最終 JSON が見つかりました。インポートに追加しました。",
    "checkpoint_manual_hint": "生成が失敗または停止しました。保存済みのチェックポイント JSON があれば、ディスクに残っています。手動でインポートするには「JSON を追加」を使ってください。",
    "imported_presets": "プリセットファイルを {count} 個読み込みました。",
    "saved_preset": "プリセットを保存しました: {path}",
    "no_image_selected": "画像が選択されていません。",
    "no_json_selected": "JSON が選択されていません。",
    "cannot_resume_checkpoint": "既存のチェックポイントは再利用/インポートできますが、この GPU ジェネレーターはチェックポイントからの再開にまだ対応していません。",
    "duplicate_image_name": "画像名の重複",
    "duplicate_image_rejected": "名前と拡張子が同じ画像が見つかりました: {names}。ファイル名を変更してから追加し直してください。",
    "locating": "現在の FH6 テンプレートを検出中...",
    "locating_wait": "最大 5 分かかることがあります。FH6 をバイナルグループエディターのまま、メニューを切り替えずにお待ちください。",
    "located": "FH6 テンプレートを検出し、検証しました。",
    "importing": "JSON を FH6 にインポート中...",
    "json_too_small": "選択した JSON の描画レイヤー数がテンプレートの使用可能容量より大幅に少ないため、ぼやけた結果になります。レイヤー数の多い JSON を選んでください。",
    "json_needs_more_template_layers": "FH で正しくカバー/適用するには境界レイヤーが 4 つ必要です。JSON の描画レイヤー数 + 4 以上のテンプレートを使ってください。",
    "safe_stop": "安全な FH6 テンプレートが見つからないため、書き込み前に停止しました。",
    "update_available_title": "アップデートがあります",
    "update_available_message": "新しいバージョンがあります。\n\n現在: v{current}\n最新: v{latest}",
    "update_open_page": "アップデートページを開く",
    "update_later": "後で",
    "update_check_failed_title": "アップデート確認に失敗",
    "update_check_failed_message": "アップデートを確認できませんでした。アプリはそのまま使用できます。\n\n{error}",
    "update_current": "最新バージョンです。",
    "changelog": "変更履歴",
    "runtime_folder": "ランタイム/キャッシュフォルダー",
    "open_runtime_folder": "ランタイムフォルダーを開く",
    "runtime_location": "ランタイム/キャッシュファイルはアプリと同じ場所に保存されます: {runtime}。FH6 プローブキャッシュ: {probe}。",
    "tutorial": """初心者向けの手順

1. GitHub Releases から単体 EXE をダウンロードしてそのまま実行します。通常は Python、.venv、バッチファイルは不要です。

2. Forza Horizon 6 を起動し、バイナルグループの作成 / バイナルグループエディターに入ります。

3. 多数のシンプルな球体レイヤーで構成されたテンプレートを読み込むか作成します。500 レイヤー以上を推奨します。インポート前にテンプレートのグループを解除してください。

4. このアプリで「JSON 生成」を開き、PNG/JPG/BMP 画像を追加して品質プロファイルを選び、生成ボタンをクリックします。

5. 「インポート」を開きます。生成した JSON を追加するか「生成した JSON を使用」をクリックします。ゲームプロファイルは Forza Horizon 6 のままにします。

6. 現在ゲーム内で読み込んでいるテンプレートの実際のレイヤー数を入力します。FH6 では通常メモリアドレスの入力は不要です。「JSON をインポート」をクリックすると、必要に応じてアプリが FH6 のレイヤーテーブルを自動検出します。

7. OpenProcess や権限のエラーで失敗する場合は、アプリを閉じて EXE を管理者として実行します。ゲームの再起動、別メニューへの移動、テンプレートの再読み込みを行った場合は、正しいレイヤー数で再度インポートしてください。

注意

- JSON 生成には同梱の GPU/OpenCL ジェネレーターを使用します。グラフィックドライバーを最新に保ってください。
- 現在の FH6 アドレスは、現在のゲームプロセスとエディター状態でのみ有効です。
- 安全なテンプレートが見つからない場合は、エディターが開いていること、テンプレートのグループが解除されていること、レイヤー数が正確であることを確認してください。

領域ペイント

領域ペイントでは、画像の特定の領域を繰り返し細かく仕上げられます。全レイヤーを一度に生成する代わりに、まずベースレイヤーを生成し、次に領域 (顔、細部など) を選択して、その領域にだけレイヤーを追加します。

1. 「領域ペイント」タブを開き、「画像を追加」で PNG/JPG/BMP を選択します。

2. 品質プロファイルを選びます。これで総予算 (プロファイルの stopAt 値) が決まります。初回パスのレイヤー数 (最初に画像全体に生成する数) と領域レイヤー数 (選択領域ごとに追加する数) を調整します。

3. 元画像キャンバスで矩形または楕円ツールを使い、選択領域を描きます。赤いオーバーレイが選択範囲です。選択を消すには「すべてクリア」を使います。

4. 「初回パスを開始」をクリックしてベースレイヤーを生成します。完了すると右のキャンバスにプレビューが表示されます。

5. 左のキャンバスに選択領域を描き、「選択領域をペイント」をクリックすると、その領域内にだけレイヤーを追加します。仕上げたい領域ごとに繰り返します。

6. すべてのパスが終わったら、「結果フォルダーを開く」で出力先の base.json を確認するか、「結果 JSON を保存」で任意の場所に書き出します。

7. 結果の JSON は「インポート」タブで通常の生成と同じ手順でインポートします。

ヒント

- 残り予算は「残り」の横に表示されます。領域パスごとにこの予算からレイヤーを消費します。
- 同じ領域に複数回の領域パスを実行して、さらに細かく仕上げられます。
""",
    "region_paint_tab": "領域ペイント",
    "region_step_image": "ステップ 1 — 画像とプロファイルを選択",
    "region_step_budget": "ステップ 2 — レイヤー予算を設定",
    "region_step_selection": "ステップ 3 — 仕上げる領域を選択",
    "region_step_actions": "ステップ 4 — 生成",
    "region_total_layers": "総予算",
    "region_first_pass_layers": "初回パスのレイヤー数",
    "region_region_layers": "領域レイヤー数",
    "region_remaining": "残り",
    "region_tool_rect": "矩形",
    "region_tool_ellipse": "楕円",
    "region_tool_brush": "ブラシ",
    "region_tool_polygon": "多角形",
    "region_tool_clear": "すべてクリア",
    "region_tool_clear_selected": "選択をクリア",
    "region_exclude_mode": "除外モード",
    "region_toggle_exclude": "含める/除外を切替",
    "region_rotation": "回転",
    "region_rotation_degrees": "{angle}°",
    "region_brush_size": "ブラシサイズ",
    "region_start_first_pass": "初回パスを開始",
    "region_paint_region": "選択領域をペイント",
    "region_stop": "停止",
    "region_pass_history": "パス履歴",
    "region_original_label": "元画像",
    "region_preview_label": "プレビュー",
    "region_preview_tab": "プレビュー",
    "region_heatmap_tab": "ヒートマップ",
    "region_no_image": "先に画像を追加してください。",
    "region_no_mask": "先に領域を選択してください。",
    "region_budget_exceeded": "残りレイヤーが不足しています (残り {remaining}、必要 {needed})。",
    "region_first_pass_done": "初回パス完了。{layers} レイヤーを使用しました。仕上げる領域を選択してください。",
    "region_pass_done": "領域パス完了。{layers} レイヤーを追加、残り {remaining}。",
    "region_no_first_pass": "領域をペイントする前に初回パスを実行してください。",
    "region_open_result_folder": "結果フォルダーを開く",
    "region_save_result_json": "結果 JSON を保存",
    "region_small_screen_hint": "(小さい画面向け)",
    "region_restore_checkpoint": "チェックポイントを復元",
    "region_checkpoint_active": "使用中",

    # Full-shape import/export (TYPECODE_TEXT keys)
    "full_shape_tab": "フルシェイプ入出力",
    "full_shape_intro_title": "実験的 FH6 フルシェイプ インポート/エクスポート",
    "full_shape_intro": "レイヤーオフセット 0x7A の 16-bit シェイプワードを使用します。研究用、手作り/エクスポートした JSON 向けの機能です。通常の生成済み楕円 JSON は引き続きインポートページを使ってください。",
    "full_shape_session_title": "ステップ 1 - FH6 セッション",
    "full_shape_session_hint": "FH6 のバイナルグループエディターを開き、対象グループを開いたまま、FH6 プロセスを更新/選択します。インポートには、保存して開き直した白い円だけのテンプレートを使い、先にグループを解除してください。",
    "full_shape_import_title": "ステップ 2 - フルシェイプ JSON をインポート",
    "full_shape_import_hint": "type-code フルシェイプ JSON を選択します。位置・拡大率・回転・スキュー・色・マスク・シェイプワードのみを書き込み、その後 FH6 グループのレイヤー数を切り詰めます。",
    "full_shape_choose_json": "フルシェイプ JSON を選択",
    "full_shape_clear_unused": "未使用のテンプレートレイヤーを消去",
    "full_shape_import_button": "フルシェイプ JSON をインポート",
    "full_shape_export_title": "現在の FH6 グループをエクスポート",
    "full_shape_export_hint": "読み取り専用のエクスポートです。エクスポートをクリックした後に JSON の出力先を選びます。JSON 書き込み前に編集中のテーブルを検証します。",
    "full_shape_export_button": "現在のグループをエクスポート",
    "full_shape_open_folder": "前回の出力フォルダーを開く",
    "full_shape_notes_title": "現在のモデルと注意事項",
    "full_shape_notes": "確認済みのモデル:\n- レイヤーオフセット 0x7A の 16-bit FH6 シェイプワードを読み書きします。\n- 安定した表示フィールドのみ書き込みます: 位置、拡大率、回転、スキュー、色、マスクフラグ、シェイプワード。\n- 0xA8 などの揮発性リソースポインターはコピーしません。\n\n推奨インポート手順:\n1. 白い円だけのテンプレートを作成して保存し、開き直してからグループを解除します。\n2. JSON のシェイプ数と一致する正確なレイヤー数を入力します。\n3. 新しいテンプレートに 1 回だけインポートします。結果はすぐに表示されます。\n\nまだ実験的な機能です。FH6 のサムネイルが更新されていないように見える場合は、レイヤーエディターに入って出てから結果を確認してください。",
    "full_shape_selected_json": "選択したフルシェイプ JSON:",
    "full_shape_invalid_json": "無効なフルシェイプ JSON",
    "full_shape_count_required": "フルシェイプのレイヤー数は正の数で指定してください。",
    "full_shape_no_json": "フルシェイプ JSON が選択されていません。",
    "full_shape_no_shapes": "フルシェイプ JSON に shapes がありません。",
    "full_shape_single_json_required": "フルシェイプ JSON は 1 つずつインポートします。一覧で JSON を 1 つ選択してから「JSON をインポート」をクリックしてください。",
    "full_shape_too_many_shapes": "フルシェイプ JSON のシェイプ数が、読み込んだテンプレートのレイヤー数を超えています。",
    "full_shape_fresh_template_required": "安全な新規 FH6 インポート用テンプレートが見つかりません。保存して開き直した白い円だけのテンプレートを読み込んでグループを解除し、FH6 をバイナルグループエディターのままにして、新しいテンプレートごとに 1 回だけインポートしてください。詳細: {detail}",
    "full_shape_probe_wait": "読み込まれた FH6 フルシェイプグループを検出中です。FH6 をバイナルグループエディターのまま、メニューを切り替えないでください。",
    "full_shape_locating": "FH6 フルシェイプグループを検出中...",
    "full_shape_importing": "フルシェイプ JSON を FH6 にインポート中...",
    "full_shape_exporting": "現在の FH6 グループをエクスポート中...",
    "full_shape_trimming": "FH6 グループのレイヤー数を切り詰め中...",
    "full_shape_run_folder": "フルシェイプ実行フォルダー",
    "export_full_shape_report": "フルシェイプレポートをエクスポート",
    "full_shape_no_report": "エクスポートできるフルシェイプレポートはまだありません。",
    "full_shape_report_export_failed": "フルシェイプレポートのエクスポートに失敗しました",
    "full_shape_report_exported": "フルシェイプレポートをエクスポートしました: {path}",
    "full_shape_non_circle_template_warning": "現在のテンプレートは新しい白い円テンプレートではありません (円レイヤー {circle}/{count})。このまま続行します。インポートに失敗したり FH6 の動作がおかしい場合は、保存済みのクリーンなテンプレートを開き直して再試行してください。",
    "full_shape_failure_prompt": "フルシェイプ操作に失敗しました。\n\nFH6 がバイナルグループエディターのままか、レイヤー数が正確か、グループが解除されているかを確認してください。インポートには保存して開き直したクリーンなテンプレートを推奨します。失敗が続く場合は「フルシェイプレポートをエクスポート」をクリックし、ZIP を送ってください。\n\n詳細: {detail}",
    "full_shape_import_done_title": "フルシェイプインポート完了",
    "full_shape_import_success_prompt": "フルシェイプインポートで {count} レイヤーを書き込みました。結果はエディターにすぐ表示されます。",
    "full_shape_import_done": "フルシェイプインポート完了: {count} レイヤーを書き込みました。",
    "full_shape_export_done": "フルシェイプエクスポート完了: {count} レイヤー -> {path}",
    "full_shape_failed": "フルシェイプ操作に失敗しました",
}
